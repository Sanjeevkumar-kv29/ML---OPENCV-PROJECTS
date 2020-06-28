import cv2
import numpy as np

def fun(x):
    pass

cv2.namedWindow('trackbar')

cv2.createTrackbar('lh','trackbar',0,255,fun)
cv2.createTrackbar('ls','trackbar',0,255,fun)
cv2.createTrackbar('lv','trackbar',0,255,fun)
cv2.createTrackbar('hh','trackbar',0,255,fun)
cv2.createTrackbar('hs','trackbar',0,255,fun)
cv2.createTrackbar('hv','trackbar',0,255,fun)

while True:

    img = cv2.imread('apples.jpg')
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('lh','trackbar')   # lh - lower hue
    ls = cv2.getTrackbarPos('ls','trackbar')   # ls - lower saturation
    lv = cv2.getTrackbarPos('lv','trackbar')   # lv - lower value
    hh = cv2.getTrackbarPos('hh','trackbar')   # hh - higher hue
    hs = cv2.getTrackbarPos('hs','trackbar')   # lh - higher saturation
    hv = cv2.getTrackbarPos('hv','trackbar')   # lh - higher value


    lb=np.array([lh,ls,lv])
    hb=np.array([hh,hs,hv])

    mask = cv2.inRange(hsv,lb,hb)

    resultimage = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('image',resultimage)

    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()