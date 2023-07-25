import cv2
import numpy as np
import matplotlib.pyplot as plt

src1 = cv2.imread('./dog1.jpg')
src2 = cv2.imread('./dog2.jpg')

alpha = 0.7

dst1 = src1 * alpha + src2 * (1-alpha)
dst1 = dst1.astype(np.uint8)

dst2 = cv2.addWeighted(src1, alpha, src2, (1-alpha), 0)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
