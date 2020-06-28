import cv2
import numpy as np


image = cv2.imread('apples.jpg')                    #main image or parent image
imggray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template = cv2.imread('appletemplate.jpg')           #template image which we want to search in main image
w = template.shape[0]
h=template.shape[1]

template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(imggray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.98  # adjust till get one value pair of left top corner

pos = np.where(res>=threshold)

for p in zip(*pos[::-1]):
  cv2.rectangle(image,p,(p[0]+w,p[1]+h),(0,0,255),2)

#print(pos)


cv2.imshow('img',image)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()