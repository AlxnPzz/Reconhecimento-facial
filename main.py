import cv2 #acessar a câmera
import mediapipe as mp #reconhecedor

#iniciar o poencv e o mediapipe

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #ler as informações
    verificador, frame = webcam.read()

    if not verificador:
        break #se não houver imagem, sair do loop

    #reconhecer os rostos
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections: #se houver rostos
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto) #desenhar o rosto


    cv2.imshow("Rostos",frame)

    # quando apertar ESC, para o loop
    if cv2.waitKey(2) == 27: #Quando aperture ESC, sair do loop
        break
webcam.release()
cv2.destroyAllWindows()
