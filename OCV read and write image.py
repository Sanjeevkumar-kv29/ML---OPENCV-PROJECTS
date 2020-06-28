import cv2

img = cv2.imread('lena.jpg',0)


# reading the img
cv2.imshow('mynewwindow',img)
k=cv2.waitKey(0)


if k==ord('s'):

    # writing the image
    cv2.imwrite('lenacopy.jpg',img)
