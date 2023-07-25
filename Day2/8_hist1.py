import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([src], [0], None, [256], [0, 255])
cv2.imshow('src', src)
plt.plot(hist)
plt.show()
cv2.waitKey()
