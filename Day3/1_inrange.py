import cv2

src = cv2.imread('./candies.png')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
'''
RGB 녹색계열
0   <= B <= 100
128 <= G <= 255
0   <= R <= 100

50  <= H <= 80
150 <= S <= 255
0   <= V <= 255
'''
dst = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
