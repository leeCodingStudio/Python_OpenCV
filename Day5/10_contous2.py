import cv2
import random

import numpy as np

img = cv2.imread('./milkdrop.bmp', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = img.shape[:2]
dst = np.zeros((h, w, 3), np.uint8)

for i in range(len(contours)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, color, 2)

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
