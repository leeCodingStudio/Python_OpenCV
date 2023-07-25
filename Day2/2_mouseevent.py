import cv2
import numpy as np
oldx = oldy = 0
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('왼쪽 버튼이 눌렸어요: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 때졌어요: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = np.ones((500, 500, 3), dtype=np.uint8) * 255
cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse, img)
cv2.imshow('img', img)
cv2.waitKey()