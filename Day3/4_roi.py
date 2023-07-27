import cv2

img = cv2.imread('./sun.jpg')
x = 182
y = 20
w = 122
h = 115
roi = img[y: y+h, x: x+w]
img2 = roi.copy()
# print(roi.shape)
img[y: y+h, x+w: x+w+w] = roi
cv2.rectangle(img, (x, y), (x+w+w, y+h), (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.imshow('roi', img2)
cv2.waitKey()