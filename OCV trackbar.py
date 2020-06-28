import cv2
import numpy as np

img = np.zeros((255,255,3),np.uint8)
cv2.namedWindow('trackbar')

def fun(x): pass

cv2.createTrackbar('track1','trackbar',0,255,fun)
cv2.createTrackbar('track2','trackbar',0,255,fun)
cv2.createTrackbar('track3','trackbar',0,255,fun)

while True:

    cv2.imshow('trackbar',img)

    b=cv2.getTrackbarPos('track1','trackbar')
    g=cv2.getTrackbarPos('track2','trackbar')
    r=cv2.getTrackbarPos('track3','trackbar')

    img[:] =[b,g,r]

    k=cv2.waitKey(1)
    if k==ord('q'):
        break


cv2.destroyAllWindows()