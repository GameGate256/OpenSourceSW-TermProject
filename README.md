# OpenSourceSW-TermProject


# 1. Hand Gesture-Based Volume Control:
by 202434862 허준서

The first part of the code uses MediaPipe Hands to detect hand landmarks in real-time from a webcam feed.
By calculating the distance between the thumb and index finger, it maps this distance to the system audio volume using Pycaw.
It visually displays the distance and current volume on the video feed, allowing the user to control volume by adjusting the gap between their thumb and index finger.

## Prerequisites

1. **Python Version**: Ensure you have Python 3.7 or higher installed.
2. **Dependencies**: Install the required libraries using pip.

```bash
pip install opencv-python mediapipe pycaw comtypes numpy
```
3. **Camera Access**: The script uses your system's default webcam. Make sure the camera is functional and accessible.

# 2. Category-Based Object Classification
by 202434862 진준하

This program uses YOLO (You Only Look Once) to detect and classify objects in real-time from a webcam feed. 
The detected objects are grouped into predefined categories such as vehicles, animals, electronics, and more. 
Each detected object is displayed on the video feed with bounding boxes and confidence scores, and the categorized results are printed in the terminal.


## Prerequisites


1. **Python Version**: Ensure you have Python 3.7 or higher installed.
2. **Dependencies**: Install the required libraries using pip.

```bash
pip install opencv-python numpy
```

pip install opencv-python numpy
YOLO Model Files:
Download the following files and place them in the same directory as your script:

yolov4.cfg: YOLOv4 configuration file.
yolov4.weights: Pre-trained YOLOv4 weights file.
coco.names: File containing class labels from the COCO dataset.
These files can be downloaded from the [YOLO official website](https://pjreddie.com/darknet/yolo/) or other trusted sources.

#4 Camera Access: The script uses your system's default webcam. Ensure your camera is functional and accessible.
