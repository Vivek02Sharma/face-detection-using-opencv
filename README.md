# Face Detection using OpenCV

[![Video](https://github.com/Vivek02Sharma/face-detection-using-opencv/assets/112774647/b046cdc1-8479-4914-96fa-cf8a573302c8)
](https://github.com/Vivek02Sharma/face-detection-using-opencv/blob/71def4bdcecc577d1d2ab056cfee1d3879827a5a/face%20detection%20output%20video.mp4)


## Overview

This GitHub repository contains a Python script that utilizes the OpenCV library for real-time face detection in a video stream. The Haar Cascade Classifier is employed to identify frontal faces within each frame of the specified video. Detected faces are highlighted with rectangles, and the processed video is displayed in a window.

## Prerequisites

Before running the script, ensure that you have OpenCV installed in your Python environment. You can install it using the following command:

```bash
pip install opencv-python
```

## Usage
**1. Clone the Repository**
```bash
git clone https://github.com/Vivek02Sharma/face-detection-using-opencv.git
```
**2. Run the Script**
```bash
python face_detection.py
```
**3. Quit the application**

Press `q` or `Q` key to exit the code.

## Code Explanation

### Dependencies
```bash
import cv2
```
Import the OpenCV library.
```bash
video = cv2.VideoCapture("src/baby_boy_video.webm")
if not video.isOpened():
    print("ERROR : Cannot open video")
    exit()
```
Open the specified video file. Check if the video is successfully opened; if not, print an error message and exit.

```bash
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
```
Load the pre-trained Haar Cascade Classifier for face detection.

```bash
while True:
    ret, frame = video.read()
    if not ret:
        print("ERROR : Failed to capture frame.")
```
Read each frame from the video. If reading fails, print an error message.

```bash
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
Flip the frame horizontally for better visualization. Convert the frame to grayscale.

```bash
    face_detect = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=6,
    )
```
Detect faces in the grayscale frame using the detectMultiScale method with specified parameters.

```bash
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
```
Draw rectangles around the detected faces in the original color frame.

```bash
    cv2.imshow("Video Windows", frame)
```
Display the processed frame in a window titled "Video Windows."

```bash
    if cv2.waitKey(1) == ord('q'):
        break
```
Check for the 'q' key press to exit the loop and close the video window.

```bash
video.release()
cv2.destroyAllWindows()
```
Release the video capture object and close all OpenCV windows.




















