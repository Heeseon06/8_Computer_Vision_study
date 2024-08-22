# 2_mouseEvent.py
import cv2
import numpy as np

oldx = oldy = 0

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요: %d, %d' % (x, y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떼졌어요: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스가 움직일 때 발생하는 이벤트를 처리
        if flags & cv2.EVENT_FLAG_LBUTTON: # 마우스 왼쪽 버튼이 눌린 상태인지
            # print('드레그중이에요: %d, %d' % (x, y)) # 드레그 중
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2. imshow('img', img)
            oldx, oldy = x, y


img = np.ones((500, 500, 3), dtype=np.uint8) * 255

cv2.namedWindow('img') # 앞으로 띄울 창이름 먼저 세팅
cv2.setMouseCallback('img', on_mouse)
cv2.imshow('img', img)
cv2.waitKey()

