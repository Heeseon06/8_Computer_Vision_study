# 7_cameraIn.py

import cv2
import sys

cap = cv2.VideoCapture(0) # 파일경로: 동영상 불러옴, 숫자: 해당 인덱스에 설치된 카메라를 불러옴 # 첫번째 등록한 카메라

if not cap.isOpened():
    print('카메라 열 수 없음')
    sys.exit() # 프로그램 여기서 종료

print('카메라 연결 성공')
print('가로 사이즈', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 설정 하기
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27: # 0.01초 동안 멈추지만 우리가 잘 모름
    # if cv2.waitKey(1000) == 27: # 1000 이면 1초마다 움직임 느림
        break

cap.release()
