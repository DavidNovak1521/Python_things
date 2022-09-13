import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

I = cv.imread("kepek/lena_szurke.png")

I = ((I - I.min()) / (I.max() - I.min()) * 255).astype(np.uint8)

H = np.zeros((256, 3))

for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        for k in range(I.shape[2]):
            H[I[i, j, k], k] += 1

H_b = cv.calcHist([I], [0], None, [256], [0, 256])
H_g = cv.calcHist([I], [1], None, [256], [0, 256])
H_r = cv.calcHist([I], [2], None, [256], [0, 256])

# elso
plt.subplot(2, 1, 1)
plt.plot(H[:, 0], color="b")
plt.plot(H[:, 1], color="g")
plt.plot(H[:, 2], color="r")

#masodik
plt.subplot(2, 1, 2)
plt.plot(H_b, color="b")
plt.plot(H_g, color="g")
plt.plot(H_r, color="r")

cv.imshow("I", I)
plt.show()
cv.waitKey()
cv.destroyAllWindows()
