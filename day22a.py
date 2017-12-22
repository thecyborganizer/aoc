#!/usr/bin/env python

grid = [list(x.rstrip()) for x in open('day22input.txt', 'r').readlines()]
#grid = [list(x.rstrip()) for x in open('day22test.txt', 'r').readlines()]


origin = (len(grid)/2, len(grid)/2)
count = 0
class facing:
    N, E, S, W = range(4)
    move = ((-1,0),(0,1),(1,0),(0,-1))

for g in grid:
    print g

def burst():
    global pos, direction, grid, count
    if grid[pos[0]][pos[1]] == '#':
        grid[pos[0]][pos[1]] = '.'
        direction = (direction + 1) % 4
    else:
        count += 1
        grid[pos[0]][pos[1]] = '#'
        direction = (direction - 1) % 4
    move = facing.move[direction]
    pos = (pos[0] + move[0], pos[1] + move[1])
    if (pos[0] >= len(grid) or pos[1] >= len(grid) or pos[0] < 0 or pos[1] < 0):
        grid = grow_grid(grid)
        pos = (pos[0] + 1, pos[1] + 1)

def grow_grid(grid):
    l = len(grid) + 2
    g = [['.' for i in range(l)] for j in range(l)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            g[i+1][j+1] = grid[i][j]
    return g
            

pos = origin
direction = facing.N
for i in xrange(10000):
    burst()

print count

