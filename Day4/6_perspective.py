import cv2
import numpy as np

img = cv2.imread('./pic.jpg')
w, h = 600, 400

srcQuad = np.array([[370, 173], [1223, 157], [1422, 844], [211, 865]], np.float32)
dstQuad = np.array([[0, 0], [w, 0], [w, h], [0, h]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img, pers, (w, h))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
