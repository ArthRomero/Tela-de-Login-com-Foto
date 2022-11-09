import cv2
import os.path

webcam = cv2.VideoCapture(0)
def foto():
    i = 1
    if webcam.isOpened():
        validaçao, frame = webcam.read()
        while(i <= 10):
            if (os.path.isfile(f"C:/Users/arthu/Desktop/Estudo/1 Sem/Projeto de Software 2/Fotos/Foto {i}.png")):
                i += 1
            else:
                cv2.imwrite(f"C:/Users/arthu/Desktop/Estudo/1 Sem/Projeto de Software 2/Fotos/Foto {i}.png", frame)
                break

    webcam.release()
    cv2.destroyAllWindows()