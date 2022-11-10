from copy import copy
from operator import imod
from re import M
from turtle import color
import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()
    

    blur = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = np.array([95,149,28])
    upper = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    ball_cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ball_cnts = imutils.grab_contours(ball_cnts)


    if (len(ball_cnts) > 0):
        c = max(ball_cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)

        if radius > 0:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,0,255), 2)

        
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break