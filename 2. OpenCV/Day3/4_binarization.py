# 4_binarization.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

# cv2.THRESH_BINARY: 픽셀값이 임계값을 넘으면 최대값으로 지정하고 넘지 못하면 0으로 지정
a, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
b, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)
print('a', a) # 임계값

cv2.imshow('src', src)
cv2.imshow('dist1', dst1)
cv2.imshow('dist2', dst2)

plt.plot(hist)
plt.show()
cv2.waitKey()
