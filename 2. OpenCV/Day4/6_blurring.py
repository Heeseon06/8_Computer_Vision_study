# 6_blurring.py
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./dog.bmp')
dst1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst2 = cv2.blur(img, (7, 7))

cv2.imshow('img', img)
cv2.imshow('dst2', dst2)


plt.figure(figsize=(10, 5))
for i, k in enumerate([5, 7, 9]):
    kernel = np.ones((k, k)) / k ** 2
    filterring = cv2.filter2D(dst1, -1, kernel)
    plt.subplot(1, 3, i+1)
    plt.imshow(filterring)
    plt.title('kernel_size:{}'.format(k))
    plt.axis('off')
plt.show()
cv2.waitKey()
