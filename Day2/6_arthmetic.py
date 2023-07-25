# square.bmp (256*256)
# 같은 크기의 이미지와 연산
# add, addWeighted, subtract, absdiff
# matplotlib의 sublpot을 이용해서 이미지 비교
import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread('./dog-icon.png')
src2 = cv2.imread('./square.bmp')

add = cv2.add(src1, src2)
addWeighted = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
subtract = cv2.subtract(src1, src2)
absdiff = cv2.absdiff(src1, src2)

img = {'add': add, 'addWeighted': addWeighted, 'subtract': subtract, 'absdiff': absdiff}

for i, (k, v) in enumerate(img.items()):
    plt.axis('off')
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)

plt.show()
