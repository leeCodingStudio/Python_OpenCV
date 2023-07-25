import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(src)

hist1 = cv2.calcHist([src], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([equ], [0], None, [256], [0, 255])

hists = {'hist1': hist1, 'hist2': hist2}

cv2.imshow('src', src)
cv2.imshow('equ', equ)

plt.figure(figsize=(12, 8))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()
