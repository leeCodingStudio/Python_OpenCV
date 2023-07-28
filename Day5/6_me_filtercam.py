import cv2
import numpy as np

cap = cv2.VideoCapture(0)
flag = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if flag % 3 == 0:
        dst = frame
    elif flag % 3 == 1:
        dst = cv2.GaussianBlur(frame, (0, 0), 3)
    else:
        med_val = np.median(frame)
        lower = int(max(0, 0.7 * med_val))
        upper = int(min(255, 1.3 * med_val))
        dst = cv2.GaussianBlur(frame, (3, 3), 0, 0)
        dst = cv2.Canny(dst, lower, upper, 10)

    cv2.imshow('dst', dst)
    key = cv2.waitKey(10)

    if key == 32:
        flag += 1
    elif key == 27:
        break

cap.release()
