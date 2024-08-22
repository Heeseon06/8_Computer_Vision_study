# 8_hist1.py
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./dog.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])

cv2.imshow('img', img)
plt.plot(hist)
plt.show()
cv2.waitKey()
