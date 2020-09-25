import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('train.xml')

image = cv2.imread('anhnhom.jpeg', 0)
# image = cv2.resize(image, (650, 551))

faces = face_cascade.detectMultiScale(image, 1.1, 4)

print((faces))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # image[y:y+h, x:x+w] = cv2.filter2D(image[y:y+h, x:x+w], cv2.CV_8U, np.ones((5,5))/25)

cv2.imshow('img', image)
cv2.waitKey()