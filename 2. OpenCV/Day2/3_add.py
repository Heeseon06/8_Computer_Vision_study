# 3_add.py
import cv2

img1 = cv2.imread('../Day1/dog.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../Day1/dog.bmp')

dst1 = cv2.add(img1, 100) # 원래있던 사진에 100 더함 => 흑백 밝아짐
dst2 = cv2.add(img2, (100, 100, 100, 0)) # (255, 255, 255, 0) 컬러 BGR 순서, 채널에는 더하면 안됨  => 컬러 밝아짐
dst3 = cv2.subtract(img1, 100) # => 어두워짐
dst4 = cv2.multiply(img1, 10) # 굉장히 밝아짐
dst5 = cv2.divide(img1, 10) # 거의 안보임 검정화면

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.imshow('dst5', dst5)

cv2.waitKey()
