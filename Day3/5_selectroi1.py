# sum.jpg 사진에서 원하는 ROI부분을 마우스로 선택하고 선택된 ROI를 창으로 출력

import cv2
import numpy as np

isDrag = False
oldx = oldy = w = h = 0
color = (255, 0, 0)
img_copy = None

def on_mouse(event, x, y, flags, param):
    global oldx, oldy, w, h, isDrag, img_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        isDrag = True
        oldx = x
        oldy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDrag:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (oldx, oldy), (x, y), color, 3)
            cv2.imshow('img', img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDrag:
            isDrag = False
            w = x - oldx
            h = y - oldy
            if w > 0 and h > 0:
                cv2.rectangle(img_copy, (oldx, oldy), (x, y), color, 3)
                cv2.imshow('img', img_copy)
                roi = img[oldy:oldy+h, oldx:oldx+w]
                cv2.imshow('roi', roi)
        else:
            cv2.imshow('img', img)
            print('영역이 잘 못 되었음')


img = cv2.imread('./sun.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()