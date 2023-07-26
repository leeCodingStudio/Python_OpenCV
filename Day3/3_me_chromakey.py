import cv2

cap = cv2.VideoCapture('./woman.mp4')
dst = cv2.VideoCapture('./background.mp4')
flag = False

while True:
    ret1, frame1 = cap.read()
    ret2, frame2 = dst.read()
    if not ret1:
        break
    if cv2.waitKey(10) == 32:
        flag = True
    elif cv2.waitKey(10) == 27:
        break

    if flag:
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame1', frame1)

cap.release()
dst.release()
