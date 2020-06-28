import cv2
import  numpy as np

shapes = cv2.imread('shapes.png')
grey = cv2.cvtColor(shapes,cv2.COLOR_BGR2GRAY)

re , thresh = cv2.threshold(grey,225,255,cv2.THRESH_BINARY)
contours , ri = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours :

    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(shapes,[approx],0,(0,0,0),2)

    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(len(approx))
    if len(approx)==3:
        cv2.putText(shapes,'triangle',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))

    elif len(approx)==4:
        cv2.putText(shapes,'rectangle',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))

    elif len(approx)==5:
        cv2.putText(shapes,'pentagon',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))

    elif len(approx)==6:
        cv2.putText(shapes,'hexagon',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))

    else:
        cv2.putText(shapes,'circle',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))


cv2.imshow('shapes',shapes)
cv2.waitKey(0)
cv2.destroyAllWindows()