import cv2

cap = cv2.VideoCapture('vtest.avi')

ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    pepcount=[]
    diff = cv2.absdiff(frame1,frame2)
    imggray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    imggray=cv2.GaussianBlur(imggray,(5,5),0)
    ret , thresh = cv2.threshold(imggray,50,255,cv2.ADAPTIVE_THRESH_MEAN_C)

    dilate = cv2.dilate(thresh,kernel=None,iterations=3)
    contours , heraichy = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    #cv2.drawContours(frame1,contours,-1,(0,255,0),3)

    #we ittrate each conture and draw rectangle

    for conture in contours:
        x,y,w,h = cv2.boundingRect(conture)

        if cv2.contourArea(conture)>500 and (w>15 and w<65) and h>40: # adjust according size of moving of object
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),1)
            pepcount.append(conture)
            cv2.imshow('res',frame1)

    cv2.putText(frame1, 'detected people - '+str(len(pepcount)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('res',frame1)
    frame1=frame2
    r ,frame2 = cap.read()

    if cv2.waitKey(40)==ord('q'):
        break


    #pepcount.clear()

cap.release()
cv2.destroyAllWindows()
