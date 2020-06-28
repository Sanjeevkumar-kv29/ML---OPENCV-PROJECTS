import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lap= cv2.Laplacian(img,cv2.CV_64F,ksize=3)

cv2.imshow('edge detection ',lap)

# we also have method sobel x and sobel y

cv2.waitKey(0)
cv2.destroyAllWindows()