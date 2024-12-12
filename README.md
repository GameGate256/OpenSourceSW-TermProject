# OpenSourceSW-TermProject


1. Hand Gesture-Based Volume Control:
The first part of the code uses MediaPipe Hands to detect hand landmarks in real-time from a webcam feed.
By calculating the distance between the thumb and index finger, it maps this distance to the system audio volume using Pycaw.
It visually displays the distance and current volume on the video feed, allowing the user to control volume by adjusting the gap between their thumb and index finger.

3. Object Detection and Categorization:
The second part uses a pre-trained YOLO (You Only Look Once) model to detect objects in real-time from the webcam feed.
Detected objects are categorized into predefined groups (e.g., vehicles, animals, electronics) based on their COCO labels.
Bounding boxes are drawn around detected objects, along with their labels and confidence scores.
Detected items are printed in groups for better categorization (e.g., listing all vehicles or animals detected).
