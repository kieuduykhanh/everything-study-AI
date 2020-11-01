import cv2

image = cv2.imread('img200x200.png')

height, width, chanels = image.shape

new_dim = (width*2, height*2)

resize_nearest = cv2.resize(image, new_dim, interpolation=cv2.INTER_NEAREST)
resize_linear = cv2.resize(image, new_dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow('abc', image)
cv2.imshow('nearest', resize_nearest)
cv2.imshow('linear', resize_nearest)

cv2.waitKey()
cv2.destroyAllWindows()