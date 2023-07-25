import cv2
import sys

cap1 = cv2.VideoCapture('./bird.mp4')
cap2 = cv2.VideoCapture('./islands.mp4')

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('bird_island.avi', fourcc, fps, (w, h))

for cap in [cap1, cap2]:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) == 27:
            break

    cap.release()