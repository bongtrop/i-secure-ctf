import math
import numpy as np
import cv2

f = open("pixel.csv", "r")

lines = f.readlines()
h = w = int(math.sqrt(len(lines)))

im = np.zeros((h,w))

ii = 0

for i in range(h):
    for j in range(w):
        line = lines[ii]
        ii+=1

        colors = line.split(",")

        im[i,j] = int(colors[0])


cv2.imshow("test", im)
cv2.waitKey(0)
