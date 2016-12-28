import cv2

print("OpenCV Version: "+cv2.__version__)

# Create the haar cascade
cascPath = "Classifier/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
camera_port = 0
cap = cv2.VideoCapture(camera_port)

while(True):

	#Take each frame
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.15,
		minNeighbors=5,
		minSize=(30, 30)
	)

	# Count the number of faces
	faceCount = format(len(faces))
	#print ("Face Count: "+faceCount)
	
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

	cv2.imshow("Face Count: "+faceCount, frame)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
