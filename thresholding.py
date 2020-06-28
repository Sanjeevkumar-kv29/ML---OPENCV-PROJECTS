import cv2
import numpy as np


img = cv2.imread('kutta.jpg')
_,kuttathresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
_,kuttathresh2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
_,kuttathresh3 = cv2.threshold(img,150,255,cv2.THRESH_MASK)
_,kuttathresh5 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
_,kuttathresh6 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)
_,kuttathresh8 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)

cv2.imshow('THRESH_BINARY',kuttathresh1)
cv2.imshow('THRESH_BINARY_INV',kuttathresh2)
cv2.imshow('THRESH_MASK',kuttathresh3)
cv2.imshow('THRESH_TOZERO',kuttathresh5)
cv2.imshow('THRESH_TOZERO_INV',kuttathresh6)
cv2.imshow('THRESH_TRUNC',kuttathresh8)


cv2.waitKey(0)
cv2.destroyAllWindows()