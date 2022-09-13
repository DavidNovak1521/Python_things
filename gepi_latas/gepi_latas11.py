import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze0.png")

# zaj
db = 10000

x = (np.random.random(db) * I.shape[0]).astype(int)
y = (np.random.random(db) * I.shape[1]).astype(int)

I[(x[:db//2], y[:db//2])] = np.array((255, 255, 255))
I[(x[db//2:], y[db//2:])] = np.array((0, 0, 0))

# szures
I_szurt = cv.medianBlur(I, 3)


cv.imshow("I", I)
cv.imshow("I szurt", I_szurt)
cv.waitKey()
cv.destroyAllWindows()
