import cv2

img = cv2.imread('./airplane.bmp')
mask = cv2.imread('./mask_plane.bmp')
dst = cv2.imread('./field.bmp')

temp = cv2.copyTo(img, mask)
cv2.copyTo(img, mask, dst)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('temp', temp)
cv2.imshow('dst', dst)
cv2.waitKey()