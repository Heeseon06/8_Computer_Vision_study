# 1_keyEvent.py
import cv2

# 이미지 읽기
img = cv2.imread('./dog.bmp')
cv2.imshow('img', img)

while True:
    keyvalue = cv2.waitKey()
    # 'i' 또는 'I' 키를 눌렀을 때 이미지 색상 반전
    if keyvalue == ord('i') or keyvalue == ord('I'):
        img = ~img
        cv2.imshow('img', img)
    # ESC 키를 눌렀을 때 프로그램 종료
    elif keyvalue == 27:
        break
