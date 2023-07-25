import cv2

img_origin = cv2.imread('./dog.bmp')
'''
img_origin = img_origin[91:210, 125:210]
img_copy = img_origin
'''
img_copy = img_origin[91:210, 125:210].copy()

cv2.imshow('img_origin', img_origin)
cv2.imshow('img_copy', img_copy)
cv2.waitKey()