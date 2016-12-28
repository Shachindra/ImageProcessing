#python detect_barcode.py --image images/barcode_01.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2
import sys

print("OpenCV Version: "+cv2.__version__)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "provide the path to the image file")
args = vars(ap.parse_args())

if args["image"] is not None:
	# load the image
	image = cv2.imread(args["image"])
	if( image is None):
		print("Error: Invalid Image!\nPlease provide a Valid Picture.")
		exit()

elif args["image"] is None:
	print("No Picture provided!\nChoosing Alternate Way...\nTaking Picture From the Webcam...")
	camera_port = 0
	cap = cv2.VideoCapture(camera_port)
	ret, image = cap.read()

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction
gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
 
# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# blur and threshold the image
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# construct a closing kernel and apply it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

# find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
if(len(cnts) > 0):
	c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
	print(len(c))
	
	# compute the rotated bounding box of the largest contour
	rect = cv2.minAreaRect(c)
	box = np.int0(cv2.boxPoints(rect))
	
	# draw a bounding box arounded the detected barcode and display the image
	cv2.drawContours(image, [box], -1, (0, 255, 0), 1)
	cv2.imshow("Barcode Detected", image)

	#cv2.imwrite("barcodedetected.jpg", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
elif(len(cnts) == 0):
	print("Error: No Barcode in the Picture!\nPlease provide Picture with the Barcode.")
