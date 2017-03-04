import cv2
import numpy as np

img = cv2.imread('102202.png',0)
rows, cols = img.shape

#res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
