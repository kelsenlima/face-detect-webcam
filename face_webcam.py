import cv2, os

COR = (0, 0, 255)
# QUER MUDAR A COR DO QUADRO, VISITE
# https://www.rapidtables.com/web/color/RGB_Color.html#color-table
BORDA = 2

xml_path = 'haarcascade_frontalface_alt2.xml'
#clf = cv2.CascadeClassifier(xml_path)
clf = cv2.CascadeClassifier(cv2.data.haarcascades + xml_path)

cap = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('q')):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), COR, BORDA)
        cv2.imshow('Video',frame)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()