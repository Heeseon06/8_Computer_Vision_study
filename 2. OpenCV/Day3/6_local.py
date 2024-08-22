# 6_local.py

# rice.png 영상을 이용하여 가로 4등분, 세로 4등분하고 자동 이진화를 적용해보자.
# 전역(자동) 이진화와 비교

import cv2
import numpy as np

img = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
_, dst1 = cv2.threshold(img, 0 ,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화
dst2 = np.zeros(img.shape, np.uint8)
bw = img.shape[1] // 4
bh = img.shape[0] // 4

for x in range(4):
    for y in range(4):
        img_ = img[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        dst_ = dst2[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
