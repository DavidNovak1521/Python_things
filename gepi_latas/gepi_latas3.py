import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze0.png").astype(float)

r, g, b = I[:, :, 2], I[:, :, 1], I[:, :, 0]

J = (r + g + b) / 3

K = 0.299 * r + 0.587 * g + 0.114 * b

L = cv.cvtColor(I.astype(np.uint8), cv.COLOR_BGR2GRAY)

cv.imshow("SZE b&w", J.astype(np.uint8))
cv.imshow("SZE b&w jobb", K.astype(np.uint8))
cv.imshow("SZE b&w konstans", L.astype(np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()
