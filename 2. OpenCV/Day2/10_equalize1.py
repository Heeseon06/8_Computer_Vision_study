# 10_equalize1.py
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(img)

hist1 = cv2.calcHist([img], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 255])

cv2.imshow('img', img)
cv2.imshow('dst', dst)

hists = {'hist1': hist1, 'hist2': hist2}

plt.figure(figsize=(12, 8))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)

plt.show()
cv2.waitKey()
# 몰려있어서 화질이 안좋음