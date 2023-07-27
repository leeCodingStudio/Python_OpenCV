import cv2
import numpy as np

img = cv2.imread('./dog.bmp')

# [1, 0, d1], [0, 1, d2]
aff = np.array([[1, 0, 150], [0, 1, 100]], dtype=np.float32)
dst = cv2.warpAffine(img, aff, (0, 0))

cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
