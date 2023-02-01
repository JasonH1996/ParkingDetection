Traffic Detection Code

These files are intended for use on a Raspberry Pi 4 and may require code modification to get project functioning properly (including changing hard-coded path strings)

Dependencies include tensorflow/examples repository and OpenCV python.

Link to tensorflow examples respository: https://github.com/tensorflow/examples

image_collect.py - script for collecting image data to train custom object detection model

traffic_capture.py - script for detecting and capturing a photo of a vehicle

detect_traffic.py - script for reading the most recent capture and applying an object detection algorithm to find the vehicle within the image

cars_normal2.tflite - the custom trained object detection model used to detect vehicles

