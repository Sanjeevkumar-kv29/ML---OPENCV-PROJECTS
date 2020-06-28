import cv2
import numpy as np


def regionofintrest(image,vertices):

    mask = np.zeros_like(image)
    matchmaskcolor = (255,)
    cv2.fillPoly(mask,vertices,matchmaskcolor)
    maskedimage = cv2.bitwise_and(image,mask)
    return maskedimage

def process(img):

    h = img.shape[0]
    w = img.shape[1]
    regionofvertices = [(0, h), (int(w / 2), int(h / 2)), (w, h)]    # reagion of intrest cordinates where we intresterd to work

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cenny = cv2.Canny(gray,50,150)                    #canny edge detection works better with gray scale image


    res = regionofintrest(cenny,np.array([regionofvertices],np.int32))  # calling the reagion of intrest function

    hough = cv2.HoughLinesP(res,1,np.pi/180,150,minLineLength=50,maxLineGap=10)

    for line in hough:
        
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('image',img)


if __name__ == '__main__':
    cap = cv2.VideoCapture('lanedetect.mp4')

    while cap.isOpened():
        re,frame = cap.read()
        process(frame)

        if cv2.waitKey(1)==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
