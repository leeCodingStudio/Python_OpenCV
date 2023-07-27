import cv2
import matplotlib.pyplot as plt

block_size = 9
img = cv2.imread('./sudoku.jpg', cv2.IMREAD_GRAYSCALE)

th, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 선명도가 높지만 노이즈도 높음
dst2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, 5)
# 선명도가 낮지만 노이즈도 낮음
dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, 5)

dic = {'img': img, 'dst1': dst1, 'dst2': dst2, 'dst3': dst3}

for i, (k, v) in enumerate(dic.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.imshow(v, 'gray')

plt.show()