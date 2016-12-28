import cv2

# read image
im = cv2.imread('102202.png')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# compute integral image
intim = cv2.integral(gray)

# normalize and save
intim = (255.0*intim) / intim.max()
cv2.imshow('result.jpg',intim)
cv2.waitKey()
#cv2.imwrite('result.jpg',intim)
