import cv2
import numpy as np

cap1 = cv2.VideoCapture('./bird.mp4')
cap2 = cv2.VideoCapture('./islands.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps1 = round(cap1.get(cv2.CAP_PROP_FPS))
fps2 = round(cap2.get(cv2.CAP_PROP_FPS))

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('homework.avi', fourcc, fps1, (w, h))

delay = fps1 * 2

for i in range(frame_cnt1 - delay):
    ret1, frame1 = cap1.read()
    cv2.imshow('output', frame1)
    out.write(frame1)
    if cv2.waitKey(10) == 27:
        break

for i, x in zip(range(delay), range(1, w, int(w/delay))):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    delay_frame = frame1
    delay_frame[:, :x] = frame2[:, :x]

    cv2.imshow('output', delay_frame)
    out.write(delay_frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2 - delay):
    ret2, frame2 = cap2.read()
    cv2.imshow('output', frame2)
    out.write(frame2)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()