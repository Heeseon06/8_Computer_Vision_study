import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import cv2
import pytesseract
import numpy as np
from paddleocr import PaddleOCR
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

def draw_text_with_bbox(draw, bbox, text, font, outline_color=(0, 255, 0), fill_color=(0, 255, 0)):
    draw.polygon([tuple(point) for point in bbox], outline=outline_color)
    draw.text((bbox[0][0], bbox[0][1] - 20), text, font=font, fill=fill_color)

def ocr_tesseract(image, lang='kor+eng'):
    d = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
    results = []
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        text = d['text'][i].strip()
        if text:
            x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
            bbox = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
            results.append((bbox, text))
    return results

def ocr_easyocr(image, lang_list=['ko', 'en']):
    reader = easyocr.Reader(lang_list)
    result = reader.readtext(image)
    results = []
    for bbox, text, prob in result:
        results.append((bbox, text))
    return results

def ocr_paddleocr(image, lang='korean'):
    ocr = PaddleOCR(use_angle_cls=True, lang=lang)
    result = ocr.ocr(image, cls=True)
    results = []
    for line in result:
        if line is None:
            continue
        for res in line:
            bbox, (text, prob) = res
            results.append((bbox, text))
    return results

def main():
    img = cv2.imread('./namecard.jpg')
    # img = cv2.imread('./namecard2.jpg')
    # img = cv2.imread('./namecard3.jpg')
    # img = cv2.imread('./plate.jpg')
    # img = cv2.imread('./plate1.jpg')
    # img = cv2.imread('./bill.jpg')
    # img = cv2.imread('./aaaa.jpg')
    # img = cv2.imread('./111.jpg')
    # img = cv2.imread('./222.jpg')


    dw, dh = 500, 500
    # dw, dh = 400, 1000
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

        # Tesseract OCR
        results_tesseract = ocr_tesseract(dst_gray)

        # EasyOCR
        results_easyocr = ocr_easyocr(dst_gray)

        # PaddleOCR
        results_paddleocr = ocr_paddleocr(dst_gray)

        # 폰트 설정
        font_path = "C:/Windows/Fonts/malgun.ttf"  # 말굽 폰트 경로
        font = ImageFont.truetype(font_path, 20)

        # Tesseract 결과 이미지 그리기
        dst_pil_tesseract = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
        draw_tesseract = ImageDraw.Draw(dst_pil_tesseract)
        for bbox, text in results_tesseract:
            print(f"Tesseract - Detected text: {text}")
            draw_text_with_bbox(draw_tesseract, bbox, text, font)
        dst_tesseract = cv2.cvtColor(np.array(dst_pil_tesseract), cv2.COLOR_RGB2BGR)

        # EasyOCR 결과 이미지 그리기
        dst_pil_easyocr = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
        draw_easyocr = ImageDraw.Draw(dst_pil_easyocr)
        for bbox, text in results_easyocr:
            print(f"EasyOCR - Detected text: {text}")
            draw_text_with_bbox(draw_easyocr, bbox, text, font)
        dst_easyocr = cv2.cvtColor(np.array(dst_pil_easyocr), cv2.COLOR_RGB2BGR)

        # PaddleOCR 결과 이미지 그리기
        dst_pil_paddleocr = Image.fromarray(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
        draw_paddleocr = ImageDraw.Draw(dst_pil_paddleocr)
        for bbox, text in results_paddleocr:
            print(f"PaddleOCR - Detected text: {text}")
            draw_text_with_bbox(draw_paddleocr, bbox, text, font)
        dst_paddleocr = cv2.cvtColor(np.array(dst_pil_paddleocr), cv2.COLOR_RGB2BGR)

        cv2.imshow('Tesseract OCR', dst_tesseract)
        cv2.imshow('EasyOCR', dst_easyocr)
        cv2.imshow('PaddleOCR', dst_paddleocr)

    cv2.imshow('img', img)
    cv2.imshow('cpy', cpy)
    cv2.waitKey()

main()


