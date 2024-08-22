# 4_perspective.py
import cv2

img = cv2.imread('./dog.bmp')
cp = (img.shape[1] / 2, img.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 30, 0.7) # 반시계30회전, 70프로 축소
dst = cv2.warpAffine(img, rot, (0, 0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
