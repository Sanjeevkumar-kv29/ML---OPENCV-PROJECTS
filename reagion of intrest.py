import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg')

# coping any area/object from image
ball = img[280:340,330:390]
plt.imshow(ball)

# paste the image into any image

img[273:333,100:160]=ball
plt.imshow(img)

plt.show()

cv2.destroyAllWindows()