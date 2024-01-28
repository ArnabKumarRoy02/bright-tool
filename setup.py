from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

VERSION = '1.1'
DESCRIPTION = 'Control Screen Brightness via fingertips.'

# Setting up
setup(
    name="bright-tool",
    version=VERSION,
    author="Arnab Kumar Roy",
    author_email="<arnabroy770@gmail.com>",
    desc=DESCRIPTION,
    
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bright-tool = bright_tool:detector'
        ]
    },
    install_requires=[
                    'opencv-python', 
                    'numpy', 
                    'mediapipe', 
                    'screen-brightness-control'],

    keywords=['python', 'video', 'brightness', 'controlling'],

    long_description=description,
    long_description_content_type="text/markdown",
)