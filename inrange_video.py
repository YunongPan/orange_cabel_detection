#!/usr/bin/env python
import cv2  
import numpy as np 
import time

cap = cv2.VideoCapture('2021-06-09-10-10-26_camera_color_image_raw.m4v')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('orange_cabel.avi',fourcc, 20.0, (width,height))


while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([5, 80, 80])
    upper_orange = np.array([15, 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    res = cv2.bitwise_and(frame, frame, mask = mask)
    img_Gaussian_res = cv2.GaussianBlur(res, (5, 5), 0)

    out.write(img_Gaussian_res)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', width, height)
    cv2.imshow('image', img_Gaussian_res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    time.sleep(.01)
cv2.destroyAllWindows()
cap.release()






