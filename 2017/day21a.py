#!/usr/bin/env python

import numpy as np

grid = [ ['.','#','.'],['.','.','#'],['#','#','#'] ]

rulelines = [x.split('=>') for x in open('day21input.txt', 'r').readlines()]

rules = {}
for i in rulelines:
    k = i[0].rstrip()
    v = [list(x) for x in i[1].lstrip().rstrip().split('/')]
    rules[k] = v

#0,0 0,1 0,2
#1,0 1,1 1,2
#2,0 2,1 2,2

#2,0 1,0 0,0
#2,1 1,1 0,1
#2,2 1,2 0,2

def rotate90ccw(shape):
    nusquare = [['.' for i in range(len(shape))] for j in range(len(shape))]
    for row in range(len(shape)):
        for col in range(len(shape)):
            nusquare[col][len(shape) - row - 1] = shape[row][col]
    return nusquare

def rotate_ccw(shape, i):
    for j in range(i):
        shape = rotate90ccw(shape)
    return shape

def hflip(shape):
    nusquare = [['.' for i in range(len(shape))] for j in range(len(shape))]
    for row in range(len(shape)):
        for col in range(len(shape)):
            nusquare[len(shape) - 1 -row][col] = shape[row][col]
    return nusquare

def vflip(shape):
    nusquare = [['.' for i in range(len(shape))] for j in range(len(shape))]
    for row in range(len(shape)):
        for col in range(len(shape)):
            nusquare[row][len(shape) - 1 - col] = shape[row][col]
    return nusquare

def lookup(shape, rules):
    for i in range(4):
        shape = rotate_ccw(shape, 1)
        k = "/".join(["".join(x) for x in shape])
        if k in rules.keys():
            return rules[k]
        hshape = hflip(shape)
        k = "/".join(["".join(x) for x in hshape])
        if k in rules.keys():
            return rules[k]
        vshape = vflip(shape)
        k = "/".join(["".join(x) for x in vshape])
        if k in rules.keys():
            return rules[k]
    print "didn't find shape!"

#print lookup(grid, rules)

#grid = lookup(grid, rules)

#print grid
for i in range(18):
    print i
    squares = []

    s = len(grid)

    if len(grid) % 2 == 0:
        for r in range(0, len(grid), 2):
            for c in range(0, len(grid), 2):
                squares.append( [col[c:c+2] for col in grid[r:r+2]] )
    elif len(grid) % 3 == 0:
        for r in range(0, len(grid), 3):
            for c in range(0, len(grid), 3):
                squares.append( [col[c:c+3] for col in grid[r:r+3]] )
    nusquares = []
    for square in squares:
        nusquares.append(lookup(square, rules))

    #print nusquares

    l = int(len(nusquares)**(1/2.0))
    rows = []
    for j in range(0,l):
        row = np.array(nusquares.pop(0))
        for i in range(1, l):
            row = np.hstack((row, np.array(nusquares.pop(0))))
        rows.append(row)
    grid = rows.pop(0)
    for i in range(len(rows)):
        grid = np.vstack((grid, rows.pop(0)))



count = 0
for r in grid:
    for c in r:
        if c == '#':
            count += 1

print count


#for i in hflip([range(3), range(3,6), range(6,9)]):
#    print i

#for i in vflip([range(3), range(3,6), range(6,9)]):
#    print i
