import cv2
import numpy as np


img = cv2.imread('lena.jpg')

kernal = np.ones((5,5),np.float32)/5

dst = cv2.filter2D(img,-1,kernal)
blur = cv2.blur(img,(5,5))
gausblur=  cv2.GaussianBlur(img,(5,5),0)
medianblur = cv2.medianBlur(img,5)
bilateralfilter = cv2.bilateralFilter(img,9,75,75)



cv2.imshow('loloimg',img)
cv2.imshow('filter 2d',dst)
cv2.imshow('blur',blur)
cv2.imshow('gaussian blur',gausblur)
cv2.imshow('median blur',medianblur)
cv2.imshow('bilatral filter',bilateralfilter)




cv2.waitKey(0)
cv2.destroyAllWindows()