# 1_roi.py
import cv2

img = cv2.imread('./sun.jpg')

# ROI 설정
# x, y, w, h
x = 182  # ROI의 시작 x 좌표 (이미지의 가로 방향에서의 시작 위치)
y = 21   # ROI의 시작 y 좌표 (이미지의 세로 방향에서의 시작 위치)
w = 122  # ROI의 너비 (복사할 영역의 가로 길이)
h = 110  # ROI의 높이 (복사할 영역의 세로 길이)

roi = img[y: y+h, x: x+w]  # 이미지에서 ROI 영역을 슬라이싱
roi_copy = roi.copy()  # ROI 영역을 새로운 이미지로 복사

# 오른쪽에 붙이기
img[y: y+h, x+w: x+w+w] = roi

# 두 태양을 박스로 감싸기
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0), 3)

cv2.imshow('img', img) # 원본 이미지
cv2.imshow('roi_copy', roi_copy) # ROI 이미지

cv2.waitKey()

