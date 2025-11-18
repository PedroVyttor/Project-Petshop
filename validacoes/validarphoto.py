import cv2

def tirar_foto(nome_arquivo):
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    if ret:
        cv2.imwrite('fotografias_fotograficas.png', frame)

    cam .release()