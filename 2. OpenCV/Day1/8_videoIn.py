# 8_videoIn.py

# 비디오 다운: https://pixabay.com/ko/

import cv2
import sys

cap = cv2.VideoCapture('./movie.mp4')

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()

print('동영상 불러오기 성공')
print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print('FPS:', int(cap.get(cv2.CAP_PROP_FPS))) # 1초당 보이는 프레임 수

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
