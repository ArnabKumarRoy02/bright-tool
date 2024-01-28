# bright-tool

Bright-tool is a Python package that enables users to control the brightness of their screens using fingertip gestures. This package utilises computer vision	technique to detect fingertips from a webcam feed and adjust the screen brightness accordingly.

## Features
 - Control screen brightness using simple fingertip gestures.
 - Uses computer vision techniques for fingertip detection.
 - Easy-to-use interface for adjusting brightness levels.
 - Compatible with various operating systems.
 - Lightweight and efficient implementation.

## Installation

You can install bright-tool via pip:

```bash
pip install bright-tool
```

## Usage

```bash
import bright_tool

# Run brightness controller
controller = bright_tool.detector()
```

## Requirements

 - Python >= 3.8
 - OpenCV
 - Numpy
 - MediaPipe
 - Screen-Brightness-Control

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

 - This package was inspired by the idea of controlling screen brightness using gestures.
 - Special thanks to the contributors and developers of OpenCV and NumPy.