import cv2
from test import objectDetection
cap=cv2.VideoCapture('istockphoto-1178560402-640_adpp_is.mp4')
cf=0
while True:
    ret,frame=cap.read()
    if ret :
         img=objectDetection(frame)
         cv2.imshow('image', img)
         cv2.waitKey(150)
    cf+=1
    if cf==150:
         break

