import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import easyocr

def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    pts = pts[idx]

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts

# EasyOCR reader 객체 생성
reader = easyocr.Reader(['ko', 'en'])  # 한국어와 영어 지원

img = cv2.imread('./namecard.jpg')

dw, dh = 700, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dst = np.zeros((dh, dw), np.uint8)

src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cpy = img.copy()
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    if len(approx) != 4:
        continue  # 사각형이 아닌 경우 무시
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2)

    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(img, pers, (dw, dh))
    dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    # EasyOCR을 사용한 텍스트 인식
    result = reader.readtext(dst)

    # PIL 이미지로 변환
    dst_pil = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(dst_pil)

    # 폰트 설정
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 말굽 폰트 경로
    font = ImageFont.truetype(font_path, 20)

    # 인식된 텍스트와 박스 그리기
    for (bbox, text, prob) in result:
        print(f"Detected text: {text} (probability: {prob:.2f})")
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        draw.rectangle([top_left, bottom_right], outline=(0, 255, 0), width=2)
        draw.text((top_left[0], top_left[1] - 20), text, font=font, fill=(0, 255, 0))

    # OpenCV 이미지로 변환
    dst = cv2.cvtColor(np.array(dst_pil), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.imshow('cpy', cpy)
cv2.imshow('dst', dst)
cv2.waitKey()
