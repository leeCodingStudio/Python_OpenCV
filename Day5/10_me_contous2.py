import cv2
import random

img = cv2.imread('./milkdrop.bmp', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(img_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# cv2.drawContours(dst, contours, -1, (0, 250, 0), 3)
for contour in contours:
    contour_area = cv2.contourArea(contour)
    if contour_area > 500:  # 물체 크기가 500 이상인 경우만 외곽선 그리기
        cv2.drawContours(dst, [contour], -1, (0, 250, 0), 3)

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
