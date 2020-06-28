import cv2
import numpy as np

img = cv2.imread('lena.jpg')
cv2.namedWindow('window')
points=[]


def clickevent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, str(x) + ' , ' + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
        cv2.imshow('window',img)


    if event==cv2.EVENT_RBUTTONDOWN:
        points.append((x,y))

        if len(points)>=2:
            cv2.line(img,points[-2],points[-1],(0,0,255),2)
            cv2.imshow('window',img)


cv2.setMouseCallback('window',clickevent)


cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()