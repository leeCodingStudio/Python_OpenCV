import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./taekwonv1.jpg')
img2 = cv2.imread('./taekwonv2.jpg')
img3 = cv2.imread('./taekwonv3.jpg')
# img4 = cv2.imread('./taekwon_v.jpg')
img4 = cv2.imread('./dr_ochanomizu.jpg')

cv2.imshow('img1', img1)
imgs = [img1, img2, img3, img4]
hists = []

for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i+1)
    plt.title('img%d' % (i+1))
    plt.axis('off')
    plt.imshow(img[:, :, ::-1])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0 ,256])
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)

# print(hists[0])
query = hists[0]
methods = {'CORREL': cv2.HISTCMP_CORREL, 'SHISQR': cv2.HISTCMP_CHISQR,
           'INTERSECT': cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA': cv2.HISTCMP_BHATTACHARYYA}

for j, (name, flag) in enumerate(methods.items()):
    print('%-10s' % name, end='\t')
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        ret = cv2.compareHist(query, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT:
            ret = ret/np.sum(query)
        print('img%d:%7.2f' % (i+1, ret), end='\t')
    print()
plt.show()
