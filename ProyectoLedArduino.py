import cv2
import numpy as np
import serial

#Valor del caso para arduino y apagado general de los leds
valr=0
camara=cv2.VideoCapture("http:/192.168.200.16:8080/video")
#camara=cv2.VideoCapture(0)
#Comunicacion con arduino
comunicacion = serial.Serial('COM3', 9600, timeout=1.0)

while(True):

    #recolectar datos de la camara
    _,frame=camara.read()
    Hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #COLORERS FILTRADOS

    #color verde
    InferiorColorverde=np.array([49, 108, 20])
    SuperiorColorverde=np.array([91, 255, 186])
    #color rojo
    InferiorColorrojo=np.array([0, 192, 102])
    SuperiorColorrojo=np.array([15, 255, 203])
    #color amarillo
    InferiorColoramarillo = np.array([18, 122, 148])
    SuperiorColoramarillo = np.array([66, 230, 222])


    #PROCESADO
    #mascara de rango de color,filtrado
    mascara=cv2.inRange(Hsv,InferiorColorverde,SuperiorColorverde)
    res = cv2.bitwise_and(frame, frame, mask=mascara)
    mascara1=cv2.inRange(Hsv,InferiorColorrojo,SuperiorColorrojo)
    res1 = cv2.bitwise_and(frame, frame, mask=mascara1)
    mascara2=cv2.inRange(Hsv,InferiorColoramarillo,SuperiorColoramarillo)
    res2 = cv2.bitwise_and(frame, frame, mask=mascara2)


    #Contorno verde
    cnts = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv2.putText(frame, "VERDE ", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            valr = 1
            comunicacion.write(str(valr).encode())


    #Contorno rojo
    cnts1 = cv2.findContours(mascara1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt1 in cnts1:
        if cv2.contourArea(cnt1) > 500:
            x, y, w, h = cv2.boundingRect(cnt1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
            cv2.putText(frame, "ROJO " , (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
            valr = 2
            comunicacion.write(str(valr).encode())
    #Contorno amarillo
    cnts2 = cv2.findContours(mascara2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt2 in cnts2:
        if cv2.contourArea(cnt2) > 500:
            x, y, w, h = cv2.boundingRect(cnt2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)
            cv2.putText(frame, "LLAVES", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            valr = 0
            comunicacion.write(str(valr).encode())


    cv2.imshow('Resultado',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

frame.release()
cv2.destroyAllWindows()