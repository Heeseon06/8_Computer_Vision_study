# chahe.py
import cv2

img = cv2.imread('./field.bmp')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

img_eq = dst.copy()
img_clahe = dst.copy()

img_eq[:, :, 0] = cv2.equalizeHist(img_eq[:, :, 0]) # 평탄화
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2BGR)  # 돌려놈

clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(4, 4))
img_clahe[: ,:, 0] = clahe.apply(img_clahe[:, :, 0])
img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img', img)
cv2.imshow('img_eq', img_eq)
cv2.imshow('img_clahe', img_clahe)
cv2.waitKey()
# 부분적으로 어두운 쪽은 더 어두워짐
