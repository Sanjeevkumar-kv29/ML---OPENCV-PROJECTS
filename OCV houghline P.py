'''

steps of hough transforme -

1 - first upload the image and change it into grayscale then after find the edge for using canny edge detection method
2 - use the hough transforme methods
3 - itrate one by one
4 - convert the infinite line into finite line

'''



import cv2
import numpy as np

img = cv2.imread('sudoku.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img,50,150)

hough = cv2.HoughLinesP(canny,1,np.pi/180 ,200,minLineLength=100,maxLineGap=10)

for line in hough:
    x1,y1,x2,y2 = line[0]

    '''
    x1 = int(np.cos(theta)*row + 1000*(-np.sin(theta)))
    y1 = int(np.sin(theta)*row + 1000*np.cos(theta))
    x2 = int(np.cos(theta)*row - 1000*(-np.sin(theta)))
    y2 = int(np.sin(theta)*row - 1000* np.cos(theta))
    '''
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('hough line P ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
