import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

img_norm1 = img.astype(np.float32)
img_norm1 = ((img_norm1 - img_norm1.min())*255 / (img_norm1.max() - img_norm1.min()))
img_norm1 = img_norm1.astype(np.uint8)

img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_norm1 = cv2.calcHist([img_norm1], [0], None, [256], [0, 255])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 255])

cv2.imshow('img', img)
cv2.imshow('img_norm1', img_norm1)
cv2.imshow('img_norm2', img_norm2)

hists = {'hist': hist, 'hist_norm1': hist_norm1, 'hist_norm2': hist_norm2}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()
