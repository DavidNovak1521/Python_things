import numpy as np
import cv2 as cv

I = cv.imread("kepek/sakktabla.png")
I_g = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

I_c = cv.Canny(I_g, 250, 255)
I_b = cv.blur(I_c, (5, 5))

# vonalak koordinatai
lines = np.squeeze(cv.HoughLinesP(I_b, 1, np.pi/180, 300))

for line in lines:
    x1, y1, x2, y2 = line
    cv.line(I, (x1, y1), (x2, y2), np.random.random(3) * 255, 3)

cv.imshow("I", I)
cv.waitKey()
cv.destroyAllWindows()
