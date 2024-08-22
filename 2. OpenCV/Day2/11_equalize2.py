# 11_equalize2.py

# ====================================================

# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread('./field.bmp') # 컬러
#
# ycrcb = []
# dst = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# ycrcb = cv2.split(dst)
# ycrcb = list(ycrcb)
# print(ycrcb)
#
# ycrcb[0] = cv2.equalizeHist(ycrcb[0])
# dst = cv2.merge(ycrcb)
# dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)
#
# cv2.imshow('img', img)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# ====================================================
# 문제
# split(), merge()를 사용하지 않고 슬라이싱과 인덱싱을 이용하여 위 예제와 동일하게 결과영상 만들기

import cv2

img = cv2.imread('./field.bmp')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
dst[:, :, 0] = cv2.equalizeHist(dst[:, :, 0])
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
