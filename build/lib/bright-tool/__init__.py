import cv2
import time
import math
import numpy as np
import mediapipe as mp
import HandTrackingModule as htm
import screen_brightness_control as sbc

def detector():
    # Setting the resolution of the Video
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)
    cap.set(cv2.CAP_PROP_FPS, 60)
    pTime = 0

    detector = htm.handDetector(detectionCon=0.9)

    minBrightness = 0
    maxBrightness = 100
    BrightBAR = 400
    BrightPER = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 10, (0, 100, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 100, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 100, 0), 3)
            cv2.circle(img, (cx, cy), 10, (0, 100, 0), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            Brightness = np.interp(length, [30, 200], [minBrightness, maxBrightness])
            BrightBAR = np.interp(length, [30, 200], [100, 0])
            BrightPER = np.interp(length, [30, 200], [0, 100])
            print(int(length), int(Brightness))
            sbc.set_brightness(Brightness)

            if length < 30:
                cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
        cv2.rectangle(img, (50, int(BrightBAR)), (85, 400), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, f'{int(BrightPER)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 0, 255), 3)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
