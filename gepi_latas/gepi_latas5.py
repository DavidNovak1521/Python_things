import numpy as np
import cv2 as cv

I0 = cv.imread("kepek/sze0.png").astype(int)
I1 = cv.imread("kepek/sze1.png").astype(int)

M = cv.imread("kepek/szemask.png").astype(int)

J = np.zeros(I0.shape)

for i in range(I0.shape[0]):
    for j in range(I0.shape[1]):
        for k in range(I0.shape[2]):
            if M[i, j, k] == 255:
                J[i, j, k] = I1[i, j, k]
            else:
                J[i, j, k] = I0[i, j, k]

M = M / 255

K = M * I1 + (1 - M) * I0

cv.imshow("SZE mask", J.astype(np.uint8))
cv.imshow("SZE mask rovid", K.astype(np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()
