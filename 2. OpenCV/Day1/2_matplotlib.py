# 2_matplotlib.py

import cv2
import matplotlib.pyplot as plt

# 그레이스케일 영상
# img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.waitKey()

# =========================================================
# # matplotlib를 통해 그레이스케일로 출력
# img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# plt.axis('off')
# plt.imshow(img, cmap = 'gray')
# plt.show()

# =========================================================
# # matplotlib를 통해 트루컬러로 출력 / matplotlib:RGB 순서, opencv:BGR 순서
# img = cv2.imread('./dog.bmp')
# plt.axis('off')
# plt.imshow(img)
# plt.show() # 순서가 달라서 파란색으로 나옴

# =========================================================
# # matplotlib를 통해 트루컬러로 출력
# img = cv2.imread('./dog.bmp') # BGR
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 순서 바꿔줌
# plt.axis('off')
# plt.imshow(img)
# plt.show() # 제대로 나옴

# =========================================================
# subplot이용하여 left plot에는 그레이스케일 영상, right plot에는 컬러영상을 출력
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

img_color = cv2.imread('./dog.bmp') # BGR
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_color)
plt.show()
