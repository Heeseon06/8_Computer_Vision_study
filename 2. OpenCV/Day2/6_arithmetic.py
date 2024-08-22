# 6_arithmetic.py

# add, addWeighted, subtract, absdiff
# absdiff(img1, img2)
# matpoltlib의 subplot을 이용하여 4가지 연산을 비교
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./dog.jpg')
img2 = cv2.imread('./square.bmp')

dst1 = cv2.add(img1, img2)
dst2 = cv2.addWeighted(img1, 0.5, img2, 0.5,0)
dst3 = cv2.subtract(img1, img2)
dst4 = cv2.absdiff(img1, img2)

img = {'dst1': dst1, 'dst2': dst2, 'dst3': dst3, 'dst4': dst4}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)

plt.show()

