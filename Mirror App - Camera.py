import cv2
import time
import datetime

cap=cv2.VideoCapture(0)
while True:
    _, frame= cap.read()
    cv2.imshow("Mirror - CVR - Press q to quit.",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
