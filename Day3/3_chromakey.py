import cv2

cap1 = cv2.VideoCapture('./woman.mp4')
cap2 = cv2.VideoCapture('./background.mp4')

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(cap1.get(cv2.CAP_PROP_FPS))
print(w)
print(h)
print(frame_cnt1)
print(frame_cnt2)
print(fps)

isKeypress = False

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    if isKeypress:
        ret2, frame2 = cap2.read()
        if not ret2:
            break

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame1', frame1)
    key = cv2.waitKey(10)

    if key == ord(' '):
        isKeypress = not isKeypress
    elif key == 27:
        break

cap1.release()
cap2.release()
