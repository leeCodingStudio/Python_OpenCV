import cv2

img = cv2.imread('./keyboard.bmp', cv2.IMREAD_GRAYSCALE)

_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)
# print(cnt)
# print(labels)
# print(stats)
# print(centroids)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]
    if area < 20:
        continue
    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
