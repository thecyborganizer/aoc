#!/usr/bin/env python

val=277678

def closest_odd_square(n):
    i = 1
    count = 0
    while True:
        if n < i * i:
            return i-2,count-1
        else:
            i = i + 2
            count = count + 1

#print closest_odd_square(val)
size = 17
center = size/2
m = [[0 for x in range(size)] for y in range(size)]
#m[1][2] = 1
m[center][center] = 1
for r in m:
    print r

def sum_adjacent(m, row, col):
    print row, col
    total = m[row+1][col] + m[row-1][col] + m[row][col+1] + m[row][col-1] + m[row+1][col+1] + m[row+1][col-1] + m[row-1][col+1] + m[row-1][col-1]
    if total > 277678:
        print total , " > 277678!"
    return total

def populate_next_square(m, size, start_row, start_col):
    y = start_row
    x = start_col
    m[y][x] = sum_adjacent(m, y, x)
    for i in range(size-2):
        y = y - 1
        m[y][x] = sum_adjacent(m, y, x)
    for i in range(1, size):
        x = x - 1
        m[y][x] = sum_adjacent(m, y, x)
    for i in range(1,size):
        y = y + 1
        m[y][x] = sum_adjacent(m, y, x)
    for i in range(1, size):
        x = x + 1
        m[y][x] = sum_adjacent(m, y, x)
    return y, x+1

    
#populate_next_square(m, 3, center, center + 1)

row = center
col = center + 1
for i in range(3,12,2):
    (row, col) = populate_next_square(m, i, row, col)

