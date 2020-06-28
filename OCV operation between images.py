import cv2
import numpy as np

img = cv2.imread('kutta.jpg')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.shape)
print(img.size)
print(img.dtype)

# merging and splitting the images
b,g,r = cv2.split(img)  #splliting the all chennels from colored image
imggray = cv2.merge((b,g,r),imggray)  # merging the color which is extracted by color image into grayscale image
cv2.imshow('kutta2',imggray)
cv2.imshow('kutta',img)

# adding two images
img1=np.zeros((512,512,3),np.uint8)
img2=img1.copy()
cv2.circle(img2,(256,256),200,(255,255,255),-1,)

# normal adding
normaladding = cv2.add(img1,img2)
cv2.imshow('normal add',normaladding)

# weighted adding
weightedadd= cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('weighted add',weightedadd)

# bit wise operation im images -

bitand = cv2.bitwise_and(img1,img1)
cv2.imshow('bit and',bitand)

bitor=cv2.bitwise_or(img1,img2)
cv2.imshow('bit or',bitor)




cv2.waitKey(0)
cv2.destroyAllWindows()