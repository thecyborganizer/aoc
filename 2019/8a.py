import numpy as np
import sys

length, width = 6, 25
#length, width = 2, 3

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
#print (np.shape(p))
#print(np.count_nonzero(p, 2))

most_nonzero = 0
most_nonzero_layer = -1
count = 0
for layer in p:
    nonzero = np.count_nonzero(layer)
    #print(nonzero)
    if nonzero > most_nonzero:
        most_nonzero = nonzero
        most_nonzero_layer = count
    count += 1
#print(fewest_zeroes, fewest_zero_layer)
print((p[most_nonzero_layer] == 2).sum() * (p[most_nonzero_layer] == 1).sum())


#print(p)

#print(picture)