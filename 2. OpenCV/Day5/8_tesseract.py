import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    pts = pts[idx]

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts


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

    # 인식된 글자에 네모 박스 그리기
    d = pytesseract.image_to_data(dst_gray, lang='kor+eng', output_type=pytesseract.Output.DICT)

    # PIL 이미지로 변환
    dst_pil = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(dst_pil)

    # 폰트 설정
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 말굽 폰트 경로
    font = ImageFont.truetype(font_path, 20)

    n_boxes = len(d['level'])
    for i in range(n_boxes):
        text = d['text'][i]
        if text.strip() != '':
            print(f"Detected text: {text}")
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            draw.rectangle([x, y, x + w, y + h], outline=(0, 255, 0), width=2)
            draw.text((x, y - 20), text, font=font, fill=(0, 255, 0))

    # OpenCV 이미지로 변환
    dst = cv2.cvtColor(np.array(dst_pil), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.imshow('cpy', cpy)
cv2.imshow('dst', dst)
cv2.waitKey()

