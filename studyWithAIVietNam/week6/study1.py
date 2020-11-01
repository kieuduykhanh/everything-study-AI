import cv2

img = cv2.imread('ruongbacthang.jpg', 0)

# height, width, chanels = img.shape

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)



cv2.imwrite('sobelX.jpg', sobelX)
cv2.imwrite('sobelY.jpg', sobelY)