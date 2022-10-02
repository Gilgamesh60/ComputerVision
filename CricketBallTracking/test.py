import cv2
import numpy as np
def objectDetection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
    (contours, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoured = cv2.drawContours(image=gray, contours=contours, contourIdx=-2, color=(0, 255, 0), thickness=1)

    return contoured