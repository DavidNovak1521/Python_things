import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze_logo.png")
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

R = cv.cornerHarris(I, 5, 5, 0.1)

R = (R - R.min()) / (R.max() - R.min()) * 255

cv.imshow("I", I)
cv.imshow("R", R.astype(np.uint8))
cv.waitKey()
cv.destroyAllWindows()
