import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while cap.isOpened():

    r,frame = cap.read()
    framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    template = cv2.imread('lopa.jpg')  # object want to detect in openstream
    templategray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    w = template.shape[0]
    h= template.shape[1]

    res = cv2.matchTemplate(framegray,templategray,cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    pos = np.where(res>=threshold)

    for p in zip(*pos[::-1]):

        cv2.rectangle(frame,p,(p[0]+w,p[1]+h),(0,0,255),2)

    cv2.imshow('template matching',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


