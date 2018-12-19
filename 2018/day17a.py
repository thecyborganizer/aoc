import numpy as np
import re
import itertools
import functools
import random
import cProfile
import time
import sys
from collections import deque
sys.setrecursionlimit(2000)

text = [x.rstrip() for x in open('day17input.txt', 'r')]
#text = text = [x.rstrip() for x in open('day17test.txt', 'r')]
clay = []

#dirs = [np.array([0,1]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1])]
dirs = [(0,1), (1,0), (-1,0), (0, -1)]

min_y = 9999999999999999
max_y = -9999999999999999
for t in text:
    vals = list(map(lambda x: int(x), re.findall(r'-?\d+', t)))
    if list(t)[0] == "x":
        for z in zip(itertools.repeat(vals[0]), range(vals[1], vals[2] + 1)):
            clay.append(z)
    elif list(t)[0] == "y":
        for z in zip(range(vals[1], vals[2] + 1), itertools.repeat(vals[0])):
            clay.append(z)

#print(clay)
sorted_x = sorted(clay, key=lambda x: (x[0], x[1]))
min_x = sorted_x[0][0]
max_x = sorted_x[-1][0]
sorted_y = sorted(clay, key=lambda x: (x[1], x[0]))
min_y = sorted_y[0][1]
max_y = sorted_y[-1][1]

#print(min_x, min_y, max_x, max_y)

grid = np.full((max_y+1, max_x+2), ".", dtype='str')

grid[0, 500] = "+"
for c in clay:
    grid[c[1], c[0]] = "#"


#grid[water[0][1], water[0][0]] = "~"
#print(grid)
#print(grid[:,494:508])
def step(water):
    global grid
    next_water = []
    for drop in water:
        possibilities = []
        found = False
        out_of_bounds = False
        new_loc = (drop[0], drop[1] + 1)
        if new_loc[1] >= grid.shape[0]:
            #grid[drop[1], drop[0]] = "|"
            found = True
            out_of_bounds = True
        elif grid[new_loc[1], new_loc[0]] == "." or grid[new_loc[1], new_loc[0]] == "|":
            found = True            

        if not found:
            dirs = [(1, 0), (-1, 0)]
            #if random.random() <= 0.5:
            #    dirs.reverse()
            for d in dirs:
                new_loc = (drop[0] + d[0], drop[1] + d[1])
                if grid[new_loc[1], new_loc[0]] == ".":
                    #grid[drop[1], drop[0]] = "|"
                    
                    found = True
                    break
            if not found:
                for d in dirs:
                    new_loc = (drop[0] + d[0], drop[1] + d[1])
                    if grid[new_loc[1], new_loc[0]] == "|":
                        #grid[drop[1], drop[0]] = "|"
                        found = True
                        break
        if found:
            grid[drop[1], drop[0]] = "|"
            if not out_of_bounds:
                next_water.append(new_loc)
                grid[new_loc[1], new_loc[0]] = "~"

        else:
            row = grid[drop[1], :]
            index = drop[0]
            next_wall = -1
            last_wall = -1
            for i in range(index, grid.shape[1]):
                if row[i] == "#":
                    next_wall = i
                    break
            for j in range(index, 0, -1):
                if row[j] == "#":
                    last_wall = j
                    break
            #if not (np.all(row[index:next_wall] == "~") and np.all(row[last_wall:index] == "~")):
            if not (np.all(row[last_wall+1:next_wall] == "~")):
                next_water.append(drop)
    return next_water

def compare(a1, a2):
    if a1[1] > a2[1]:
        return True
    elif a1[1] == a2[1]:
        if a1[0] < a2[0]:
            return True
        elif a1[0] >= a2[0]:
            return False
    else:
        return False

def spread(pos, from_drop):
    global grid
    global drop_set
    right_pos = (pos[0] + 1, pos[1])
    left_pos = (pos[0] - 1, pos[1])
    right_wall = False
    left_wall = False
    char_at_pos = grid[right_pos[1], right_pos[0]]
    if char_at_pos == "~":
        return
    while char_at_pos != "#":
        below = (right_pos[0], right_pos[1] + 1)
        if grid[below[1], below[0]] == "." or grid[below[1], below[0]] == "|":
            break
        right_pos = (right_pos[0] + 1, right_pos[1])
        char_at_pos = grid[right_pos[1], right_pos[0]]
    if char_at_pos == "#":
        right_wall = True
    char_at_pos = grid[left_pos[1], left_pos[0]]

    while char_at_pos != "#":
        below = (left_pos[0], left_pos[1] + 1)
        if grid[below[1], below[0]] == "." or grid[below[1], below[0]] == "|":
            break
        left_pos = (left_pos[0] - 1, left_pos[1])
        char_at_pos = grid[left_pos[1], left_pos[0]]
    if char_at_pos == "#":
        left_wall = True
    if left_wall and right_wall:
        grid[pos[1], left_pos[0]+1:right_pos[0]] = "~"
        return False
    else:
        grid[pos[1], left_pos[0]+1:right_pos[0]] = "|"
        drop_set.remove(from_drop)
        if left_wall:
            #print("go down right")
            #down_queue.appendleft(right_pos)
            drop_set.add(right_pos)
            #go_down(right_pos)
        if right_wall:
            #print("go down left")
            #down_queue.appendleft(left_pos)
            drop_set.add(left_pos)
            #go_down(left_pos)
        if (not left_wall) and (not right_wall):
            drop_set.add(right_pos)
            drop_set.add(left_pos)
            #down_queue.appendleft(right_pos)
            #down_queue.appendleft(left_pos)
            #go_down(left_pos)
            #go_down(right_pos)
        return True

def go_down(pos, spread_queue):
    global grid
    below = (pos[0], pos[1] + 1)
    char_at_pos = grid[below[1], below[0]]
    while char_at_pos != "~" and char_at_pos != "#":
        below = (below[0], below[1] + 1)
        if below[1] >= grid.shape[0]:
            grid[pos[1]:below[1], pos[0]] = "|"

            return
        char_at_pos = grid[below[1], below[0]]
    grid[pos[1]:(below[1]-1), pos[0]] = "|"
    spread_queue.appendleft(((below[0], below[1] - 1), pos))
    #spread((below[0], below[1] - 1))


#spread((500, 6))
spread_queue = deque()
#down_queue = deque()
drop_set = set()
drop_set.add((500, 0))
for i in range(15000):
    for drop in drop_set:
        go_down(drop, spread_queue)
    while len(spread_queue) > 0:
        spread_queue_item = spread_queue.pop()
        spread(spread_queue_item[0], spread_queue_item[1])
    #if i == 51:
    #    print("got here")
    #print(i)
    #if i % 100 == 0:
    #    print(i)
    #if len(down_queue) == 0 and len(spread_queue) == 0:
    #    down_queue.appendleft((500, 0))

    #down_queue = deque(sorted(down_queue)[0:50])
    #while(len(down_queue) > 0):
    #    go_down(down_queue.pop(), spread_queue)
    #while len(spread_queue) > 0:
    #    spread(spread_queue.pop(), down_queue)

#go_down((500, 0))

# for j in range(min_y, max_y+1):
#     for i in range(min_x, max_x + 1):
#         print(grid[j, i], end="")
#     print("")
# print("")


# water = []
# last_tildes = -1
# last_bars = -1
# count = 0
# for i in range(1000):
#     count += 1
#     next_water = step(water)
#     next_water.append((500, 0))
#     grid[0, 500] = "~"
#     water = sorted(next_water, key=lambda x: (x[1], x[0]), reverse=True)
#     #water = sorted(next_water, key=)
#     if count % 100 == 0:
#         print(count)
#     #with open('out.txt', "w") as f:
#     for j in range(min_y, max_y+1):
#         for i in range(min_x, max_x + 1):
#             print(grid[j, i], end="")
#         print("")
#     print("")

tildes = (grid[1:max_y+1, min_x:max_x+1] == "~").sum()
bars = (grid[1:max_y+1, min_x:max_x+1] == "|").sum()
print(tildes, bars, tildes+bars)

with open('out.txt', "w") as f:
    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x + 1):
            print(grid[j, i], end="", file=f)
        print("", file=f)
print((grid[min_y:max_y+1, min_x:max_x+1] == "~").sum() + (grid[min_y:max_y+1, min_x:max_x+1] == "|").sum())