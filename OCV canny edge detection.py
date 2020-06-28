import cv2


img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img,200,255)

cv2.imshow('canny edge ',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()