import numpy as np
import cv2 as cv

I = cv.imread("kepek/waldo.png")
T = cv.imread("kepek/waldo_minta.png")

w = I.shape[1]
h = I.shape[0]

wt = T.shape[1]
ht = T.shape[0]

M0 = np.zeros((h, w))

for i in range(w - wt):
    for j in range(h - ht):
        roi = I[j:j+ht, i:i+wt]
        M0[j, i] = np.sum(np.abs(roi - T))

_, _, min_idx, _ = cv.minMaxLoc(M0[:h-ht, :w-wt])

cv.circle(I, (min_idx[0] + wt // 2, min_idx[1] + ht // 2), 30, (0, 0, 255), 2)
cv.rectangle(I, (min_idx[0], min_idx[1]), (min_idx[0] + wt, min_idx[1] + ht), (255, 0, 0), 2)

cv.imshow("I", I)
cv.imshow("T", T)
cv.waitKey()
cv.destroyAllWindows()
