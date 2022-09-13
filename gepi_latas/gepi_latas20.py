import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze_logo_regi.png")

I_nn = cv.resize(I, None, fx=25, fy=25, interpolation=cv.INTER_NEAREST)
I_lin = cv.resize(I, None, fx=25, fy=25, interpolation=cv.INTER_LINEAR)
I_cubic = cv.resize(I, None, fx=25, fy=25, interpolation=cv.INTER_CUBIC)

cv.imshow("I", I)
cv.imshow("nearest", I_nn)
cv.imshow("linear", I_lin)
cv.imshow("cubic", I_cubic)
cv.waitKey()
cv.destroyAllWindows()
