# 5_copyImg.py

import cv2

img = cv2.imread('./dog.bmp')
# img_test = img # => 같은 위치에 찍힘
img_test = img.copy() # 원본 그대로 있고 다른곳에 카피해서 만듬 => 없으면 같은 위치 가르킴

img_test[90:210, 120:240] = (255, 102, 255)

cv2.imshow('img', img)
cv2.imshow('img_test', img_test)
cv2.waitKey()