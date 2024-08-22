# 7_color.py
import cv2

img = cv2.imread('./candies.png')
print('shape: ', img.shape)
print('dtype: ', img.dtype)

# b = img[:, :, 0]
# g = img[:, :, 1]
# r = img[:, :, 2]
b, g, r = cv2.split(img) # 결과 똑같음

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.waitKey()
