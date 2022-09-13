import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze0.png")

J = np.zeros(I.shape, dtype=np.uint8)

K = np.zeros(I.shape, dtype=np.uint8)

for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        for k in range(I.shape[2]):
            J[i, j, k] = 255 - I[i, j, k]

K = 255 - I

cv.imshow("SZE I", I)
cv.imshow("SZE J", J)
cv.imshow("SZE K", K)
cv.waitKey(0)
cv.destroyAllWindows()
