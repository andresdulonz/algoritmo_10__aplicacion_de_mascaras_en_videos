import cv2

img = cv2.imread('Captura.PNG')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_i = cv2.inRange(hsv,(54,223,221),(60,229,227))

mask = cv2.bitwise_not(mask_i)
img_2 = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Imagen original',img)
cv2.imshow('Imagen 2',img_2)
cv2.waitKey(0)