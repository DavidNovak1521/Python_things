import numpy as np
import cv2 as cv

I0 = cv.imread("kepek/sze0.png").astype(int)
I1 = cv.imread("kepek/sze1.png").astype(int)

I_sum = I0 + I1

I_sum_A = I_sum / 510 * 255

I_sum_B = np.zeros(I_sum.shape)
"""
for i in range(I_sum.shape[0]):
    for j in range(I_sum.shape[1]):
        for k in range(I_sum.shape[2]):
            if I_sum[i, j, k] > 255:
                I_sum_B[i, j, k] = 255
            else:
                I_sum_B[i, j, k] = I_sum[i, j, k]
"""
I_sum_B = (I_sum <= 255) * I_sum + (I_sum > 255) * 255

cv.imshow("SZE sum", I_sum.astype(np.uint8))
cv.imshow("SZE sum A", I_sum_A.astype(np.uint8))
cv.imshow("SZE sum B", I_sum_B.astype(np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()
