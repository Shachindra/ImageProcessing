import cv2
import time

cascPath = "Classifier/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)

def getImage():
	retval, im = camera.read()
	return im
	
for i in xrange(ramp_frames):
	temp = getImage()

image = getImage()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

timeNow = time.strftime("%Y-%m-%d_%H-%M-%S_%Z")
print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite("./FaceDetected/FaceDetected_"+timeNow+".jpg", image)
cv2.waitKey(0)