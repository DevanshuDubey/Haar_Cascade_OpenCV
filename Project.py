import cv2
import os
import pandas as pd

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
bounding_boxes = []

folder_path = "TestImages"
image_files = [f"img{i}.jpg" for i in range(1, 13)]
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayimage, scaleFactor=1.2, minNeighbors=6, minSize=(40, 40))

    for (x, y, w, h) in faces:
        bottom_left = (x, y + h)
        top_right = (x + w, y)
        bounding_boxes.append([image_file, bottom_left, top_right])

        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    output_path = os.path.join('OutputImages', f"output_{image_file}")
    cv2.imwrite(output_path, image)

df = pd.DataFrame(bounding_boxes, columns=['Image', 'Bottom-Left', 'Top-Right'])
df.to_csv('bounding_boxes.csv', index=False)

print("done.")
