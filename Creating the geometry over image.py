import cv2

img = cv2.imread('lena.jpg')

# drawing the line over the image
img = cv2.line(img,(0,0),(510,510),(0,0,152),2)

# drawing the arrow line over the image
img = cv2.arrowedLine(img,(0,100),(200,100),(0,255,0),2)

# drawing the rectangle over the image
img = cv2.rectangle(img,(100,150),(200,200),(155,0,0),3)

# drawing the circle over the image
img = cv2.circle(img,(300,300),100,(250,250,250),2)


cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()