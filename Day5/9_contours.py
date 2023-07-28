import cv2
import random

img = cv2.imread('./contours.bmp', cv2.IMREAD_GRAYSCALE)
contours, _ = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(color)
cv2.drawContours(dst, contours, -1, color, 3)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
