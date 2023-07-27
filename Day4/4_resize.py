import cv2

img = cv2.imread('./dog.bmp')
dst1 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1[400:800, 200:600])
cv2.imshow('dst2', dst2[400:800, 200:600])
cv2.waitKey()

