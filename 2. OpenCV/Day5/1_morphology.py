import cv2
import numpy as np

img = cv2.imread('./circuit.bmp', cv2.IMREAD_GRAYSCALE)
# gse = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# gse = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
gse = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 3))

dst1 = cv2.dilate(img, gse)
dst2 = cv2.erode(img, gse)

cv2.imshow('img' ,img)
cv2.imshow('dst1' ,dst1) # 선이 넓어짐 => 팽창
cv2.imshow('dst2' ,dst2) # 선이 얇아짐 => 침식

cv2.waitKey()
