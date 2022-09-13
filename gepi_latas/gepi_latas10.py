import numpy as np
import cv2 as cv

cap = cv.VideoCapture("kepek/boja.mp4")

while(cap.isOpened()):
    _, frame = cap.read() # nem kell az elso visszaadott ertek
    frame = cv.resize(frame, None, fx=0.5, fy=0.5)
    #cv.imshow("f", frame.astype(np.uint8))
    
    b, g, r = cv.split(frame)

    filtered = ((r > 100) * (g < 50) * (b < 50)) * 255

    merged = cv.merge((filtered, filtered, filtered))

    frame = np.where(merged == 255, (0, 255, 0), frame)

    idx = np.argwhere(merged[:, :, 0] == 255)
    x = int(np.sum(idx[:, 0]) / idx.shape[0])
    y = int(np.sum(idx[:, 1]) / idx.shape[1])

    #frame = cv.circle(frame, (y, x), 10, (255, 0, 0), -1) # itt hiba

    cv.imshow("frame", frame.astype(np.uint8))
    
    if cv.waitKey(1) == ord("q"):
        print("\n'q' clicked\n")
        break

cv.destroyAllWindows()
cap.release()
