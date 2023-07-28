import cv2

img = cv2.imread('./noise.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.medianBlur(img, 3)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
