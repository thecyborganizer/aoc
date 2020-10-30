import numpy as np
import sys

length, width = 6, 25
#length, width = 2, 2

picture = []
#with open("8test.txt") as f:
with open("8input.txt") as f:
    t = f.readline()
    layer_length = length*width
    for i in range(int(len(t)/(layer_length))):
        layer = t[i*layer_length:(i+1)*layer_length]
        rows = []
        for j in range(int(len(layer)/width)):
            row = layer[j*width:(j+1)*width]
            pixels = []
            for k in range(len(row)):
                pixel = int(row[k:k+1])
                pixels.append(pixel)
            rows.append(pixels)
        picture.append(rows)

p = np.array(picture)
o = np.zeros_like(p[0])
for i in range(length):
    for j in range(width):
        stack = p[:,i, j]
        for k in range(len(stack)):
            if stack[k] != 2:
                break
        if stack[k] == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

