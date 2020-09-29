import cv2

#doc video

video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    top = (450, 150)
    bottom = (750, 550)

    cv2.rectangle(img, top, bottom, (128,  128, 128), 1)

    cv2.imshow('img', img)

    # press the 'a' key
    if cv2.waitKey(33) == ord('a'):
        break

rectangle = gray[150:550, 450:750]
w, h = rectangle.shape[::-1]
cv2.imshow('rectangle', rectangle)
cv2.waitKey(0)

while True:
    _, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corr_map = cv2.matchTemplate(gray, rectangle, cv2.TM_CCOEFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_map)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)



    cv2.rectangle(img, top_left, bottom_right, (128,  128, 128), 1)

    cv2.imshow('img', img)

    # press the 'a' key
    if cv2.waitKey(33) == ord('a'):
        break