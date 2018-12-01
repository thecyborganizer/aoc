#!/usr/bin/env python

def reverse_range(l, i, length):
    if length > len(l):
        return l
    if i + length < len(l):
        r = l[i:i+length]
        r.reverse()
        return l[0:i] + r + l[i+length:]
    else:
        overflow = i + length - len(l)
        r = l[i:] + l[0:overflow]
        r.reverse()
        to_return = r[len(r) - overflow:] + l[overflow:i] + r[0:len(r) - overflow]
        return to_return
       

def knot_hash(s):
    sparse = range(256)

    lengths = [ord(x) for x in list(s)] + [17, 31, 73, 47, 23]

    cur_pos = 0
    skip_size = 0


    for i in range(64):
        for length in lengths:
            sparse = reverse_range(sparse, cur_pos, length)
            cur_pos = (cur_pos + length + skip_size) % len(sparse)
            skip_size += 1

    dense = []
    for i in range(0, len(sparse), 16):
        b = 0
        for j in range(16):
            b = b ^ sparse[i + j]
        dense.append(b)

    return "".join([format(x, '02x') for x in dense])

def count_bits(k):
    i = int(k, 16)
    return (i & 0x1) + ((i & 0x2) >> 1) + ((i & 0x4) >> 2)  + ((i & 0x8) >> 3)

def set_bits(k, row, col):
    global grid
    i = int(k, 16)
    shift = 3
    for j in range(col*4, col*4 + 4):
        grid[row][j] = (i >> shift) & 0x1
        shift -= 1

def floodfill(g, row, col, val):
    if row < 0 or col < 0 or row > 127 or col > 127 or g[row][col] != 1:
        return False
    g[row][col] = val
    floodfill(g, row-1, col, val)
    floodfill(g, row+1, col, val)
    floodfill(g, row, col+1, val)
    floodfill(g, row, col-1, val)
    return True



def print_grid(g):
    for r in g:
        print "".join([str(i % 10) for i in r])

#input_str = "flqrgnkx"
input_str = "ugkiagan"
grid = [[0 for i in range(128)] for j in range(128)]
for i in range(128):
    l = knot_hash(input_str + "-" + str(i))
    for j in range(len(list(l))):
        set_bits(l[j], i, j)

val = 2
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if floodfill(grid, row, col, val):
            val += 1

#print_grid(grid)

print max([max(l) for l in grid]) - 1
