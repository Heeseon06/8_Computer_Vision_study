# 4_blending.py
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./man.jpg')
img2 = cv2.imread('./turkey.jpg')

# 다른이유
# img1 + img2: 255를 넘어갈 경우 해당값의 256을 빼서 표현
dst1 = img1 + img2
# cv2.add(): 255를 넘어갈 경우 255로 고정
dst2 = cv2.add(img1, img2)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()

img = {'img1': img1, 'img2': img2, 'dst1': dst1, 'dst2': dst2}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()
