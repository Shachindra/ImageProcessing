import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#cv2.NamedWindow("webcam", 1)
#capture = cv2.CaptureFromCAM(-1)
img = cv2.QueryFrame(capture)
cv2.SaveImage("CamPics/cameraPic01.jpg", img)
