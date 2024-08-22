# 3_selectROI2.py
import cv2

img = cv2.imread('./sun.jpg')

x, y, w, h = cv2.selectROI('img', img, False)
# True => 창문 모양 네모
# False => 그냥 네모 모양

if w and h:
    roi = img[y: y+h, x: x+w]
    cv2.imshow('roi', roi)

cv2.waitKey()

# 부분 선택하고
# 엔터누르면 영역이 나눠짐