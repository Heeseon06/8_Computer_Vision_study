import cv2
import random

img = cv2.imread('./contours.bmp', cv2.IMREAD_GRAYSCALE)

# hierarchy: 계층정보
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
print('contours: ', contours)
print('hierarchy: ', hierarchy)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print('color: ', color)

cv2.drawContours(dst, contours, -1, color, 3)
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
# 외곽선을 잘 그림
