# python3 FaceDetection.py Classifier/haarcascade_frontalface_default.xml Images/camPic01.jpg 
# Refactored https://realpython.com/blog/python/face-recognition-with-python/

# import the necessary packages
import numpy as np
import argparse
import time
import cv2
import sys

print("OpenCV Version: "+cv2.__version__)

# Detect Face in the Picture
def cascade_detect(cascade, image):
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	return cascade.detectMultiScale(
		gray_image,
		scaleFactor = 1.15,
		minNeighbors = 5,
		minSize = (30, 30)
	)

# Draw the rectangle on the face detected
def detections_draw(image, detections):
	for (x, y, w, h) in detections:
		print ("({0}, {1}, {2}, {3})".format(x, y, w, h))
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

# main() Function
def main(argv = None):
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", "--classifier", required = False, help = "provide the path to the haar cassifier file")
	ap.add_argument("-i", "--image", required = False, help = "provide the path to the image file")
	ap.add_argument("-r", "--resultpath", required = False, help = "provide the path to save the face-detected picture")
	args = vars(ap.parse_args())

	if args["classifier"] is not None:
		# load the classifier
		cascade_path = args["classifier"]
		print("Classifier Provided!")
	elif args["classifier"] is None:
		print("No classifier provided!\nChoosing Default Location...")
		cascade_path = "Classifier/haarcascade_frontalface_default.xml"

	if args["image"] is not None:
		# load the image
		print("Picture Provided!")
		image = cv2.imread(args["image"])
		if( image is None):
			print("Error: Invalid Image!\nPlease provide a Valid Picture.")
			exit()
	elif args["image"] is None:
		print("No Picture provided!\nChoosing Alternate Way...\nTaking Picture From the Webcam...")
		camera_port = 0
		cap = cv2.VideoCapture(camera_port)
		ret, image = cap.read()
	
	if args["resultpath"] is not None:
		# load the classifier
		result_path = args["resultpath"]
		print("Result Path to Folder Provided!")
	elif args["resultpath"] is None:
		print("No Result Path to Folder provided!\nChoosing Default Location...")
		timeNow = time.strftime("%Y-%m-%d_%H-%M-%S_%Z")
		result_path = "FaceDetected/FaceDetected_"+timeNow+".jpg"
	
	cascade = cv2.CascadeClassifier(cascade_path)
	detections = cascade_detect(cascade, image)
	detections_draw(image, detections)
	
	# Count the number of faces
	faceCount = int(format(len(detections)))
	
	if faceCount == 0:
		print ("No Face Found")
	elif faceCount == 1:
		print ("1 Face Found")
		cv2.imshow("1 Face Found!", image)
		cv2.imwrite(result_path, image)
	elif faceCount > 1:
		print ("Face Count: "+str(faceCount))
		cv2.imshow(str(faceCount)+" Faces Found!", image)
		cv2.imwrite(result_path, image)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	sys.exit(main())
