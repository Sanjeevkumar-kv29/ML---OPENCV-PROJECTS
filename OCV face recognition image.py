import cv2
import numpy as np

facemodel = cv2.CascadeClassifier('frontalface.xml')
# load image to detect the face in images
img = cv2.imread('student.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

detectedfaces = facemodel.detectMultiScale(gray,1.1,10)
detectcount = []

for (x,y,w,h) in detectedfaces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.circle(img,(x+25,y+25),50,(0,255,255),2)
    detectcount.append(x)

cv2.putText(img,'DETECTED FACES = '+str(len(detectcount)),(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)


cv2.imshow('lolo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()