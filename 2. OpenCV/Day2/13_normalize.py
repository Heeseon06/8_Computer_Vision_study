import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])

cv2.imshow('img', img)
cv2.imshow('img_norm', img_norm)

hists = {'hist': hist, 'hist_norm': hist_norm}

for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()