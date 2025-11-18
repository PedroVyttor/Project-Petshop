import cv2

#def tirar_foto(nome_arquivo):
#    cam = cv2.VideoCapture(1)

    #ret, frame = cam.read()

   #if ret:
        #cv2.imwrite('foto.png', frame)

    #cam .release()

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

if ret:
    cv2.imwrite('foto.png', frame)

cam .release()