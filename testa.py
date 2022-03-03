import cv2 as cv


img = cv.imread("images/bruce lee5.jpg")
cv.imshow("bruce", img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("bruce_gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3 )
    

print("number of faces= ", len(faces_rect))

cv.waitKey(0)