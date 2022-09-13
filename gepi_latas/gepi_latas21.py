import numpy as np
import cv2 as cv

I = cv.imread("kepek/lena.png")

xd = 10
yd = -5

xs = 1.5
ys = 0.7

r = np.radians(30)

# tolas
T1 = np.array(((1, 0, xd),
                (0, 1, yd),
                (0, 0, 1)))

# meretezes
T2 = np.array(((xs, 0, 0),
                (0, ys, 0),
                (0, 0, 1)))

#forgatas
T3 = np.array(((np.cos(r), np.sin(r), 0),
                (-np.sin(r), np.cos(r), 0),
                (0, 0, 1)))

T = np.dot(T1, np.dot(T2, T3))

J = np.zeros(I.shape)

for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        p = np.array((i, j, 1))
        q = np.dot(T, p)
        u = round(q[0])
        v = round(q[1])
        if 0 < u < I.shape[1] and 0 < v < I.shape[0]:
            J[u, v] = I[i, j]

cv.imshow("I", I)
cv.imshow("J", J.astype(np.uint8))
cv.waitKey()
cv.destroyAllWindows()
