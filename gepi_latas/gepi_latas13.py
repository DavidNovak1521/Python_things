import numpy as np
import cv2 as cv

I = cv.imread("kepek/m.png")

k = np.ones((9, 9))

I_close = cv.morphologyEx(I, cv.MORPH_CLOSE, k)

# zaj
db = 10000

x = (np.random.random(db) * I.shape[0]).astype(int)
y = (np.random.random(db) * I.shape[1]).astype(int)

I_close[(x, y)] = np.array((255, 255, 255))

I_open = cv.morphologyEx(I_close, cv.MORPH_OPEN, k)

cv.imshow("I", I)
cv.imshow("I close", I_close)
cv.imshow("I open", I_open)
cv.waitKey()
cv.destroyAllWindows()
