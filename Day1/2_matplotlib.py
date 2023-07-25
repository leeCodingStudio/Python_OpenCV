import cv2
import matplotlib.pyplot as plt

'''
img_gray = cv2.imread('dog.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img_gray', img_gray)
cv2.waitKey()
'''

'''
img_gray = cv2.imread('dog.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')
plt.show()
'''

'''
# cv2.IMREAD_COLOR는 생략 가능
img_rgb = cv2.imread('dog.bmp', cv2.IMREAD_COLOR)
# GBR을 RGB로 변환
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img_rgb)
plt.show()
'''

img_gray = cv2.imread('dog.bmp', cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.imread('dog.bmp', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_rgb)
plt.show()
