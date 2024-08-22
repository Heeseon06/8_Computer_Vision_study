# 5_otsu.py
import cv2

img = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

th, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print('otsh', th)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey()

# 자동으로 이진화해서 나옴
# 이진화시키는 이유 =>
# 일단 돋보인다
# 찾기 쉽다
# 노이즈가 잘 보여서 제거하기 쉽다
# 뽑아내기 너무 좋음
