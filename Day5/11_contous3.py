import cv2
import math

def setLevel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 2)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

img = cv2.imread('./polygon.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

_, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contours)

for pts in contours:
    if cv2.contourArea(pts) < 200:
        continue
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    print(approx)
    vtc = len(approx)
    print(vtc)

    if vtc == 3:
        setLevel(img, pts, 'TRI')
    elif vtc == 4:
        setLevel(img, pts, 'RECT')
    else:
        length = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        ratio = 4. *math.pi * area / (length * length)
        if ratio > 0.70:
            setLevel(img, pts, 'CIR')
        else:
            setLevel(img, pts, 'NONAME')

# cv2.imshow('gray', gray)
# cv2.imshow('img_bin', img_bin)
cv2.imshow('img', img)
cv2.waitKey()
