import cv2
import numpy as np

img = np.full((500, 500, 3), 255, np.uint8)

cv2.line(img, (70, 70), (200, 70), (0, 0, 255), 5)
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), -1) # (x, y, w, h)
cv2.circle(img, (300, 100), 50, (255, 255, 0), -1)

str = 'Hello OpenCV'
cv2.putText(img, str, (30, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey()