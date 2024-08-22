# 5_addWeighted.py
import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./man.jpg')
img2 = cv2.imread('./turkey.jpg')

alpha = 0.7
dst1 = cv2.addWeighted(img1, alpha, img2, (1-alpha), gamma=0)
dst2 = img1 * alpha + img2 * (1-alpha)
dst2 = dst2.astype(np.uint8)

img = {'img1': img1, 'img2': img2, 'dst1': dst1, 'dst2': dst2}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()
