import cv2
import numpy as np


def empty(x):
    pass

cv2.namedWindow("RangosHSV")
cv2.createTrackbar("H Max", "RangosHSV", 179, 179, empty)
cv2.createTrackbar("H Min", "RangosHSV", 0, 179, empty)
cv2.createTrackbar("S Max", "RangosHSV", 255, 255, empty)
cv2.createTrackbar("S Min", "RangosHSV", 0, 255, empty)
cv2.createTrackbar("V Max", "RangosHSV", 255, 255, empty)
cv2.createTrackbar("V Min", "RangosHSV", 0, 255, empty)

#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("http:/192.168.200.16:8080/video")
while True:

    ret,frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_max = cv2.getTrackbarPos("H Max", "RangosHSV")
    h_min = cv2.getTrackbarPos("H Min", "RangosHSV")
    s_max = cv2.getTrackbarPos("S Max", "RangosHSV")
    s_min = cv2.getTrackbarPos("S Min", "RangosHSV")
    v_max = cv2.getTrackbarPos("V Max", "RangosHSV")
    v_min = cv2.getTrackbarPos("V Min", "RangosHSV")

    Inf = np.array([h_min, s_min, v_min])  # minumos
    Sup = np.array([h_max, s_max, v_max])  # maximos

    print("Valores de HSV")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    mask = cv2.inRange(hsv, Inf, Sup)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("VideoCamara", frame)
    cv2.imshow("MascaraDeFiltrado", mask)
    cv2.imshow("Resultado", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()