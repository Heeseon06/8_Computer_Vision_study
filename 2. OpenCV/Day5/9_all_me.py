import os
import sys

import cv2
import numpy as np
import easyocr
import pytesseract
from paddleocr import PaddleOCR
from PIL import Image, ImageDraw, ImageFont

# OpenMP 오류 방지를 위해 환경 변수 설정
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 이미지 로드
# img = cv2.imread('./namecard.jpg')
# img = cv2.imread('./namecard2.jpg')
# img = cv2.imread('./namecard3.jpg')
img = cv2.imread('./222.jpg')
if img is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인하세요.")
    sys.exit()

h, w = img.shape[:2]
dh = 500
dw = round(dh * 297 / 210)

srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)

dragSrc = [False, False, False, False]

def drawROI(img, corners):
    cpy = img.copy()
    c1 = (192, 192, 255)
    c2 = (128, 128, 255)

    for pt in corners:
        cv2.circle(cpy, tuple(pt.astype(int)), 25, c1, -1)

    cv2.line(cpy, tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, 2)

    return cpy

def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, img

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                dragSrc[i] = True
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                srcQuad[i] = (x, y)
                cpy = drawROI(img, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break

disp = drawROI(img, srcQuad)
cv2.namedWindow('img')
cv2.setMouseCallback('img', onMouse)
cv2.imshow('img', disp)

while True:
    key = cv2.waitKey()
    if key == 13:
        break
    elif key == 27:
        sys.exit()

# Perspective transform 적용
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img, pers, (dw, dh), flags=cv2.INTER_CUBIC)

cv2.imshow('dst', dst)

# EasyOCR 사용
reader = easyocr.Reader(['ko', 'en'])
result_easyocr = reader.readtext(dst)

dst_easyocr = dst.copy()
dst_pil_easyocr = Image.fromarray(cv2.cvtColor(dst_easyocr, cv2.COLOR_BGR2RGB))
draw_easyocr = ImageDraw.Draw(dst_pil_easyocr)
font_path = "C:/Windows/Fonts/malgun.ttf"
font = ImageFont.truetype(font_path, 20)

for (bbox, text, prob) in result_easyocr:
    print(f"EasyOCR Detected text: {text} (score: {prob})")
    box = np.array(bbox).astype(int)
    draw_easyocr.polygon([tuple(p) for p in box], outline=(0, 255, 0))
    draw_easyocr.text((box[0][0], box[0][1] - 20), text, font=font, fill=(0, 255, 0))

dst_easyocr = cv2.cvtColor(np.array(dst_pil_easyocr), cv2.COLOR_RGB2BGR)

# PaddleOCR 사용
ocr = PaddleOCR(use_angle_cls=True, lang='korean')
result_paddleocr = ocr.ocr(dst, cls=True)

dst_paddleocr = dst.copy()
dst_pil_paddleocr = Image.fromarray(cv2.cvtColor(dst_paddleocr, cv2.COLOR_BGR2RGB))
draw_paddleocr = ImageDraw.Draw(dst_pil_paddleocr)

for line in result_paddleocr[0]:
    box = line[0]
    txt = line[1][0]
    score = line[1][1]
    print(f"PaddleOCR Detected text: {txt} (score: {score})")
    box = np.array(box).astype(int)
    draw_paddleocr.polygon([tuple(p) for p in box], outline=(0, 255, 0))
    draw_paddleocr.text((box[0][0], box[0][1] - 20), txt, font=font, fill=(0, 255, 0))

dst_paddleocr = cv2.cvtColor(np.array(dst_pil_paddleocr), cv2.COLOR_RGB2BGR)

# Tesseract 사용
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(dst_rgb)
text = pytesseract.image_to_string(pil_img, lang='kor+eng')
print("Tesseract Detected text:")
print(text)

boxes = pytesseract.image_to_boxes(pil_img, lang='kor+eng')
dst_tesseract = dst.copy()
dst_pil_tesseract = Image.fromarray(cv2.cvtColor(dst_tesseract, cv2.COLOR_BGR2RGB))
draw_tesseract = ImageDraw.Draw(dst_pil_tesseract)

for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    y = dst_pil_tesseract.height - y
    h = dst_pil_tesseract.height - h
    draw_tesseract.rectangle([x, h, w, y], outline=(0, 255, 0))
    draw_tesseract.text((x, h - 20), b[0], font=font, fill=(0, 255, 0))

dst_tesseract = cv2.cvtColor(np.array(dst_pil_tesseract), cv2.COLOR_RGB2BGR)

# 결과 이미지 표시
cv2.imshow('result_easyocr', dst_easyocr)
cv2.imshow('result_paddleocr', dst_paddleocr)
cv2.imshow('result_tesseract', dst_tesseract)

cv2.waitKey(0)




