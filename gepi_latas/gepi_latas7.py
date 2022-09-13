import numpy as np
import cv2 as cv

I = cv.imread("kepek/sze0.png")
H = cv.imread("kepek/halalcsillag.png")

I_g = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

# mask
I_m = np.zeros(I.shape)
I_m[:, :, 0] = I_m[:, :, 1] = I_m[:, :, 2] = (I_g < 220)

#J = I + (1-I_m) * H
J = np.where(I_m, I, I.astype(int) + H.astype(int))
J = J / J.max() * 255

cv.imshow("Yeee", J.astype(np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()
