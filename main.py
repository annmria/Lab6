import cv2
from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('training_data.yml')
cascadePath = 'haar_face.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

#iniciate id counter
id = 0

people = ['Depp', 'Jackson', 'Johnson', 'Lee', 'Willis']
#reading the image:
img = cv2.imread('images/Depp/johnny depp4.jpg') # placeholder

while True:
    # färg till svartvit
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(grayimg,
        scaleFactor = 1.2,
        minNeighbors = 5,
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = face_recognizer.predict(grayimg[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = people[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
    cv2.imshow('images', img)
    
    break




