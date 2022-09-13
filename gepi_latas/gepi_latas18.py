import numpy as np
import cv2 as cv

I = cv.imread("kepek/waldo.png")
T = cv.imread("kepek/waldo_minta.png")

w = I.shape[1]
h = I.shape[0]

wt = T.shape[1]
ht = T.shape[0]

M1 = cv.matchTemplate(I, T, cv.TM_CCOEFF)

_, _, _, max_idx = cv.minMaxLoc(M1)

cv.circle(I, (max_idx[0] + wt // 2, max_idx[1] + ht // 2), 30, (0, 255, 0), 2)
cv.rectangle(I, (max_idx[0], max_idx[1]), (max_idx[0] + wt, max_idx[1] + ht), (255, 0, 0), 2)

M1_intenzitas = (M1 - M1.min()) / (M1.max() - M1.min()) * 255

cv.imshow("I", I)
cv.imshow("T", T)
cv.imshow("intenzitas", M1_intenzitas.astype(np.uint8))
cv.waitKey()
cv.destroyAllWindows()
