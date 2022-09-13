import numpy as np
import cv2 as cv

I = cv.imread("kepek/lena.png")
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

J = cv.Canny(I, 50, 200)

cv.imshow("Canny", J)

cv.waitKey(0)
cv.destroyAllWindows()
