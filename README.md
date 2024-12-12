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

# 2. Object Detection and Categorization:
The second part uses a pre-trained YOLO (You Only Look Once) model to detect objects in real-time from the webcam feed.
Detected objects are categorized into predefined groups (e.g., vehicles, animals, electronics) based on their COCO labels.
Bounding boxes are drawn around detected objects, along with their labels and confidence scores.
Detected items are printed in groups for better categorization (e.g., listing all vehicles or animals detected).


Required Libraries:
OpenCV: For capturing webcam feed and visualizing results.
Install with: pip install opencv-python
MediaPipe: For hand gesture detection.
Install with: pip install mediapipe
Pycaw: For controlling the system audio volume.
Install with: pip install pycaw
Numpy: For mathematical operations.
Install with: pip install numpy
Comtypes: For Pycaw compatibility with Windows.
Install with: pip install comtypes


YOLO Configuration and Weights Files:

yolov4.cfg: The YOLO model's configuration file.
yolov4.weights: The pre-trained weights for the YOLO model.
Download these from the official YOLO website or other trusted sources for YOLOv4.
COCO Names File:

coco.names: Contains the list of object labels YOLO can detect.
Often provided along with YOLO configuration files or can be found online.
