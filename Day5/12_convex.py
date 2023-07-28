import cv2

img = cv2.imread('./hat.png')
cpy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contour, _ = cv2. findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contour[1])
cnt = contour[1]
cv2.drawContours(img, [cnt], -1, (255, 0, 0), 2)
check = cv2.isContourConvex(cnt)
print(check)
