import numpy as np
import cv2 as cv

I = cv.imread("kepek/m.png")

k = np.ones((9, 9))

I = cv.morphologyEx(I, cv.MORPH_CLOSE, k)

cv.imshow("I", I)
cv.waitKey()
cv.destroyAllWindows()
