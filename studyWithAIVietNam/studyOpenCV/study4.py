import numpy as np
import cv2

image = cv2.imread('noise.png')
cv2.imshow('before', image)

image = cv2.medianBlur(image, 3)

cv2.imshow('after', image)

cv2.waitKey(0)
cv2.destroyAllWindows()