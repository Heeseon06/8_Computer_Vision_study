# 3_imgInfo.py

import cv2

# 흑백
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img_gray type: ', type(img_gray))
print('img_gray shape: ', img_gray.shape) # (세로, 가로)
print('img_gray dtype: ', img_gray.dtype)

# 컬러
img_color = cv2.imread('./dog.bmp')
print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape) # (세로, 가로, 채널)
print('img_color dtype: ', img_color.dtype)

# 이미지 사이즈 확인(높이 * 너비)
h, w = img_color.shape[:2]  # 0,1 까지 채널전까지만 가져옴
print(f'이미지 사이즈: {w}*{h}')

# 그레이스케일 영상인지, 컬러영상 구분하기
if len(img_color.shape) == 3:
    print('컬러 영상')
elif len(img_gray.shape) == 2:
    print('그래이스케일 영상')

# img_color에 특정 색 정보로 영상을 출력
# BGR: (255, 102, 255)
# # 방법1 => AI에서는 for문 잘 안씀
# for x in range(h):
#     for y in range(w):
#         img_color[x, y] = (255, 102, 255)
#
# cv2.imshow('img_color', img_color)
# cv2.waitKey()

# =========================================================
# 방법2 => 더 좋은 방법
img_color[::] = (255, 102, 255)
cv2.imshow('img_color', img_color)
cv2.waitKey()



