import cv2
import numpy as np


def regionofintrest(image,vertices):

    mask = np.zeros_like(image)
    # colourchannel = image.shape[2]     it is required only for colured image
    matchmaskcolor=(255,) # * colourchannel
    cv2.fillPoly(mask,vertices,matchmaskcolor)
    maskimg = cv2.bitwise_and(image,mask)
    return maskimg




def process(img):


    h = img.shape[0]
    w = img.shape[1]
    regionofvertices=[(0,h),(int(w/2),int(h/2)+50),(w,h)]

    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(imggray,100,200)

    res = regionofintrest(canny,np.array([regionofvertices],np.int32))

    hough = cv2.HoughLinesP(res,1,np.pi/180,150,minLineLength=75,maxLineGap=20)

    for line in hough:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('road',img)


if __name__ == '__main__':
    img = cv2.imread('lane.jpg')
    process(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
