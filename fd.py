import cv2
import numpy as np
face_cascade =cv2.CascadeClassifier("C:\\Users\\hp\\Desktop\\opcv\\FaceDetect-master\\haarcascade_frontalface_default.xml")
#eye_cascade =cv2.CascadeClassifier("C:\\Users\\hp\\Desktop\\opcv\\FaceDetect-master\\haarcascade_eye.xml")
cap=cv2.VideoCapture("C:\\Users\\hp\\Pictures\\Camera Roll\\nn.mp4")
a=1
while True:
  a=a+1
  ret, img=cap.read()
  #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(img , 1.3 , 5)
  for (x, y, w, h) in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #roi_color=img[y:y+h, x:x+h]
    #eyes=eye_cascade.detectMultiScale(roi_color)
    #for (ex,ey,eh,eh) in eyes:
    #	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

  cv2.imshow('nn',img)
  key=cv2.waitKey(1)
  if(key==ord('q')):
    break

cap.release()
cv2.destroyAllWindows()
