import cv2

img = cv2.imread('./sun.jpg')

x, y, w, h = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)

cv2.waitKey()