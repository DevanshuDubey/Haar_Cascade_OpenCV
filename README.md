# Overview
## Face Detection using Haar Cascade
This project uses OpenCV's pre-trained Haar Cascade classifier to detect faces in a set of images.
It processes images from the TestImages folder, detects faces, draws bounding boxes, and saves results in OutputImages.
The coordinates of detected faces are stored in a CSV file for further analysis.


---
Output Format
Each row in bounding_boxes.csv contains:
Image, Bottom-Left, Top-Right
img1.jpg, (x1, y1), (x2, y2)
img2.jpg, (x3, y3), (x4, y4)
...
