import cv2

src = cv2.imread('./field.bmp')

'''
ycrcb = []
dst = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb = cv2.split(dst)
ycrcb = list(ycrcb)
# print(ycrcb)

ycrcb[0] = cv2.equalizeHist(ycrcb[0])
dst = cv2.merge(ycrcb)
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)
'''

dst = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
dst[:, :, 0] = cv2.equalizeHist(dst[:, :, 0])
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()