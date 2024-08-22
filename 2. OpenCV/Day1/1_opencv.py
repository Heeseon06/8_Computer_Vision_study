# 1_opencv.py

import cv2

print('현재 openCV 버전: ', cv2.__version__)

# 그레이스케일 영상
# img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# # print(img)
# cv2.imshow('img', img) # 창이름, 영상
# cv2.waitKey() # 키를 입력할 때까지 대기 # 엔터치면 꺼짐

# 트루컬러 영상
img = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR 생략 가능
print(img)

cv2.imshow('img', img) # 창이름, 영상
cv2.waitKey()

