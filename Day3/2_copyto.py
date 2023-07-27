import cv2

src = cv2.imread('./airplane.bmp')
mask = cv2.imread('./mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./field.bmp')

# 출력영상을 넣지 않으면 새로 영상을 만들어 냄
# 입력영상과 마스크, 출력영상의 크기가 같아야 함
cv2.copyTo(src, mask, dst)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
