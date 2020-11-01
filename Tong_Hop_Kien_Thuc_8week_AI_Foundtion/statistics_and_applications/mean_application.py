import numpy as np
import cv2

# đọc ảnh dạng xám
image = cv2.imread('mrbean.jpg', 0)

# tạo kernel 3 * 3
kernel = np.ones((3,3), np.float32) / 9.0

# tính mean trong mỗi kernel
blurred = cv2.filter2D(image, cv2.CV_8U, kernel)

# show ảnh
cv2.imshow('image', image)
cv2.imshow('blurred', blurred)

# bấm phím bất kì để end
cv2.waitKey(0)
cv2.destroyAllWindows()