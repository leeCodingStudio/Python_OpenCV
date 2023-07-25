import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread('./dog1.jpg')
src2 = cv2.imread('./dog2.jpg')

dst1 = src1 + src2
dst2 = cv2.add(src1, src2)

img = {'src1': src1, 'src2': src2, 'dst1': dst1, 'dst2': dst2}

for i, (k, v) in enumerate(img.items()):
    plt.axis('off')
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)

plt.show()