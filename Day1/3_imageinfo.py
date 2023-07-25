import cv2

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img_gray type: ', type(img_gray))
print('img_gray shape: ', img_gray.shape) # (364, 548), (h, w)
print('img_gray dtype: ', img_gray.dtype)

img_color = cv2.imread('./dog.bmp')
print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape)
print('img_color dtype: ', img_color.dtype)

# img_color의 가로*세로
# 548*364
h, w = img_color.shape[:2]
print(f'img_color 사이즈: {w}*{h}')

# 그레이스케일 영상과 컬러 영상을 구별하는 방법
if len(img_gray.shape) == 2:
    print('img_gray는 그레이스케일입니다')
elif len(img_gray.shape) == 3:
    print('img_gray는 컬러 영상입니다')

# img_color에 특정 색 정보로 영상 출력
# BGR: (255, 102, 255)

'''
for x in range(h):
    for y in range(w):
       img_color[x, y] = (255, 102, 255)
'''
img_color[:, :] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()
