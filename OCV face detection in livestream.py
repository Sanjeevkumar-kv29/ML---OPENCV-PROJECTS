import cv2
facemodel = cv2.CascadeClassifier('frontalface.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    re,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    detectedface = facemodel.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in detectedface:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('face recognition',frame)

    if cv2.waitKey(1)==ord('q'): break

cap.release()
cv2.destroyAllWindows()
