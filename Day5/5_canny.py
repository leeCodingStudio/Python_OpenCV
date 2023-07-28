import cv2
import numpy as np

img = cv2.imread('dog.bmp')
med_val = np.median(img)
lower = int(max(0, 0.7*med_val))
upper = int(min(255, 1.3*med_val))

dst = cv2.GaussianBlur(img, (3, 3), 0, 0)
dst = cv2.Canny(dst, lower, upper, 3)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey()
