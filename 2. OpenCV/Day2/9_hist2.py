# 9_hist2.py

# dog.bmp 영상을 컬러로 불러와 3채널을 계산하여 히스토그램 그리기
# 단, 하나의 plot에서 BGR 그래프를 그리기(색상을 다르게 표현)
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./dog.jpg')

colors = ['b', 'g', 'r']
bgr = cv2.split(img)

for (b, c) in zip(bgr, colors):
    hist = cv2.calcHist([b], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)

cv2.imshow('img', img)
plt.show()

cv2.waitKey()