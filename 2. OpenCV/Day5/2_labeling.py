# labeling.py
import cv2

img = cv2.imread('./keyboard.bmp', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)

print('cnt: ', cnt)  # cnt:  38 => 원래 18인데, 20 정도는 노이즈로 잡혔다
print('labels: ', labels)
print('stats: ', stats)
print('centroids: ', centroids)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]
    if area < 30:
        continue
    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('img', img)
cv2.imshow('img_bin', img_bin)
cv2.imshow('dst', dst)
cv2.waitKey()

