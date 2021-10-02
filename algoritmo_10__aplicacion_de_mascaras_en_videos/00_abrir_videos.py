import cv2
from time import sleep

# Abrir archivo de video
cap = cv2.VideoCapture('video.mp4')

# Leer la primera imagen del archivo de video
#rec, im = cap.read()
#cv2.imshow('imagen', im)
#cv2.waitKey()

# Mostrar 50 frames
#for i in range(50):
    #rec, im = cap.read()
    #cv2.imshow('imagen', im)
    #cv2.waitKey(100)

# Mostrar todo el video
while cap.isOpened(): # revisar que el video esté abierto
    ret, im = cap.read()
    # revisar que haya más frames
    if ret == False:
        break
    cv2.imshow('imagen', im)
    # Salida con tecla ESC
    if cv2.waitKey(1) == 27:
        break
    
    sleep(1/30)
