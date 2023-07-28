import cv2

img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.GaussianBlur(img, (0, 0), 3)
dst2 = cv2.blur(img, (5, 5))

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
