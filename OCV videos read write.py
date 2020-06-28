import cv2

cap = cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*'XVID')
recording = cv2.VideoWriter('demovideo.avi',fourcc,20.0,(640,480))


while (cap.isOpened()):
    rt,frame=cap.read()

    if rt==True:

        recording.write(frame)       # RECORDING THE VIDEO BY FRAMES PER SECOND
        cv2.putText(frame,'quit-q \n capture-c',(20,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),0,cv2.LINE_AA)
        cv2.imshow('frames',frame)   # SHOWING THE VIDEO BY FRAMES PER SECOND


        if cv2.waitKey(1)==ord('c'):

            #capturing the image from live streming
            cv2.imwrite('lolo.jpg',frame)
            cv2.putText(frame, 'captured', (int(frame.shape[0]/2),int(frame.shape[1]/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 0, cv2.LINE_AA)
        if cv2.waitKey(1)==ord('q'):    # FOR QUIT THE VIDEO OF STOP THE RECORDING
            break



cap.release()
recording.release()                     # RELEASING THE RESOURCES
cv2.destroyAllWindows()
