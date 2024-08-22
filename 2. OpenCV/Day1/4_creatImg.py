# 4_creatImg.py

import cv2
import numpy as np

img1 = np.zeros((240, 320, 3), dtype = np.uint8) # 세로 가로 채널  # 검정
img2 = np.empty((240, 320), dtype = np.uint8) # 쓰레기값 
img3 = np.ones((240, 320), dtype = np.uint8) * 130  # 그레이
img4 = np.full((240, 320, 3), (255, 102, 255), dtype = np.uint8)  # 핑크



cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey()


