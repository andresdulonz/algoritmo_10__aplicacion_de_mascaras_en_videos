import cv2
from time import sleep

# Abrir archivo de video
cap = cv2.VideoCapture('video.mp4')

# Ancho y alto del video
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Code para archivo de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Archivo de salida
# 30 --> fps
out = cv2.VideoWriter('out.mp4', fourcc, 30, (w,h))

# Mostrar todo el video
while cap.isOpened(): # revisar que el video esté abierto
    ret, im = cap.read()
    # revisar que haya más frames
    if ret == False:
        break
    # Rectangulo --> variable, esq. superior, esq. inferior, color, ancho de linea
    cv2.rectangle(im, (200, 100), (600, 500), (0, 0, 255), 10)
    cv2.imshow('imagen', im)
    # gravación del video
    out.write(im)
    sleep(1/30)
    # Salida con tecla ESC
    if cv2.waitKey(1) == 27:
        break
