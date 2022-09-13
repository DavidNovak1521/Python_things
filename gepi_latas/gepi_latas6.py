import numpy as np
import cv2 as cv

I0 = cv.imread("kepek/sze_cam_0.png")
I1 = cv.imread("kepek/sze_cam_1.png")

I0 = cv.resize(I0, None, fx=0.5, fy=0.5)
I1 = cv.resize(I1, None, fx=0.5, fy=0.5)

I0 = cv.cvtColor(I0, cv.COLOR_BGR2GRAY).astype(int)
I1 = cv.cvtColor(I1, cv.COLOR_BGR2GRAY).astype(int)

##### 0 - 255
#I = I0 - I1
#I_diff_0 = np.where(I < 0, I * -1, I)

I_diff_0 = np.abs(I0 - I1)

cv.imshow("diff", I_diff_0.astype(np.uint8))

##### mas tartomany
I_diff = I0 - I1
I_diff_1 = (I_diff - I_diff.min()) / (I_diff.max() - I_diff.min()) * 255

cv.imshow("diff 1", I_diff_1.astype(np.uint8))

##### kiemeles
I_diff_2 = np.where(I_diff_0 > 20, 255, 0)

cv.imshow("diff 2", I_diff_2.astype(np.uint8))

cv.waitKey(0)
cv.destroyAllWindows()
