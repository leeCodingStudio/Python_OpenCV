import cv2

print('현재 opencv 버전: ', cv2.__version__)

# 컬러영상(BGR), cv2.IMREAD_GRAYSCALE: 그레이스케일
img = cv2.imread('./dog.bmp')
cv2.imshow('img', img) # 창이름, 영상
cv2.waitKey()