import numpy as np
import cv2 as cv

I = cv.imread("kepek/lena.png")
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

k0 = np.array(( (0, 1, 0), 
                (1, -4, 1), 
                (0, 1, 0)))

k1 = np.array(( (1, 1, 1), 
                (1, -8, 1), 
                (1, 1, 1)))
"""
I_d_2 = np.zeros(I.shape)
I_d_4 = np.zeros(I.shape)

for i in range(1, I.shape[0] - 1):
    for j in range(1, I.shape[1] - 1):
        I_roi = I[i-1:i+2, j-1:j+2]
        I_d_2[i, j] = max(0, min(255, np.sum(k0 * I_roi)))
        I_d_4[i, j] = max(0, min(255, np.sum(k1 * I_roi)))
"""

I_d_4_cv = cv.filter2D(I, -1, k1)

I_d_4_cv_ = cv.filter2D(I, cv.CV_64F, k1)

#cv.imshow("I_d_2", I_d_2.astype(np.uint8))
#cv.imshow("I_d_4", I_d_4.astype(np.uint8))
cv.imshow("I_d_4_cv", I_d_4_cv)
cv.imshow("I_d_4_cv_", I_d_4_cv_)

cv.waitKey(0)
cv.destroyAllWindows()
