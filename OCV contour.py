import cv2

img = cv2.imread('building.jpg')
imgcpy = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(imgcpy,200,255,cv2.THRESH_BINARY)

contour , herarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,contour,-1,(0,0,255),1)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()