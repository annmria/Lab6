import os
import cv2 as cv
import numpy as np

# create list of images of people (eg, ben affleck, dwayne johnson,)
people = [' ', ' ', ' ']
# pathway to folder, genom DIR = r'pathway'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
    path = os.path.join(DIR, person)
    label = people.index(person)
    
    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        
        img_array = cv.imread(img_path)
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
        
        faces_rect = # haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        
        for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w] # roi = area of interest
            features.append(faces_roi)
            labels.append(label)
            
create_train()
print('Training done')
# train the recognizer on the features list and the labels list

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)


np.save('feature.npy', features)
np.save('labels.npy', labels)

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')