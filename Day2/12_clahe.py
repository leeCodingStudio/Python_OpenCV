import cv2

img = cv2.imread('./field.bmp')
ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

img_eq = ycc.copy()
img_eq[:, :, 0] = cv2.equalizeHist(img_eq[:, :, 0])
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2BGR)

img_clahe = ycc.copy()
clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
img_clahe[:, :, 0] = clahe.apply(img_clahe[:, :, 0])
img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img', img)
cv2.imshow('img_eq', img_eq)
cv2.imshow('img_clahe', img_clahe)
cv2.waitKey()
