import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('Winnie.jpg')
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)

cv2.namedWindow('Control Panel')
cv2.resizeWindow('Control Panel', 640, 320)

cv2.createTrackbar('Hue Min', 'Control Panel', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'Control Panel', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Control Panel', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Control Panel', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Control Panel', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Control Panel', 255, 255, empty)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'Control Panel')
    h_max = cv2.getTrackbarPos('Hue Max', 'Control Panel')
    s_min = cv2.getTrackbarPos('Sat Min', 'Control Panel')
    s_max = cv2.getTrackbarPos('Sat Max', 'Control Panel')
    v_min = cv2.getTrackbarPos('Val Min', 'Control Panel')
    v_max = cv2.getTrackbarPos('Val Max', 'Control Panel')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('reslut', result)
    cv2.waitKey(1)

