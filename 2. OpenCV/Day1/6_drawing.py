# 6_drawing.py

import cv2
import numpy as np

img = np.full((500, 500, 3), 255, np.uint8)
# 선
cv2.line(img, (70, 70,), (400, 70), (0, 0, 255), 5) # 선

# 박스
# cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 3) # 박스
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), -1) # 박스 =>-1: 색상을 채움

# 원
cv2.circle(img, (300, 400), 50, (255, 0, 0), 3) # 원

# 텍스트
cv2.putText(img, 'Hello OpenCV!', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0)) # 텍스트

cv2.imshow('img', img)
cv2.waitKey()


