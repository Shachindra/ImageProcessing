import cv2
import numpy as np
print("OpenCV Version: "+cv2.__version__)
camera_port = 0
cap = cv2.VideoCapture(camera_port)

while(True):

	#Take each frame
	ret, frame = cap.read()

	#Operations on the frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#cv2.namedWindow('Webcam Feed - Grayscale', cv2.WINDOW_NORMAL)
	cv2.imshow('Webcam Feed - Grayscale', gray)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;
	elif k == ord('s'):
		cv2.imwrite("CamPics/cameraPic.jpg", frame)
		break;
cap.release()
cv2.destroyAllWindows()
