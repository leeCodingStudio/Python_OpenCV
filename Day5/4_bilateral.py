import cv2

img = cv2.imread('./gaussian_noise.jpg', cv2.IMREAD_GRAYSCALE)
dst1 = cv2.GaussianBlur(img, (5, 5), 0)
dst2 = cv2.bilateralFilter(img, 5, 80, 80)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
