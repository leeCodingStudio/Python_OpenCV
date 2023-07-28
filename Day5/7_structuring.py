import cv2

img = cv2.imread('./circuit.bmp', cv2.IMREAD_GRAYSCALE)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(img, se)
dst2 = cv2.dilate(img, None) # 3*3

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
