import cv2
import numpy as np

img = cv2.imread('sudoku.png')
imggry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(imggry,50,150)
cv2.imshow('image ',canny)

hough=cv2.HoughLines(canny,1,np.pi/180,200)

for line in hough:
    row , theta = line[0]
    x1 = int(np.cos(theta)*row + 1000*(-np.sin(theta)))
    y1 = int(np.sin(theta)*row + 1000*(np.cos(theta)))

    x2 = int(np.cos(theta)*row - 1000*(-np.sin(theta)))
    y2 = int(np.sin(theta)*row - 1000 * np.cos(theta))

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('hough lines',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
