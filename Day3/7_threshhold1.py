import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

a, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
b, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)
print(a)
print(b)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

plt.plot(hist)
plt.show()
cv2.waitKey()
