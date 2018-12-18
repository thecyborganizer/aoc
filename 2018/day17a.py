import numpy as np
import re
import itertools
import functools
import random
import cProfile
import time

text = [x.rstrip() for x in open('day17input.txt', 'r')]
#text = text = [x.rstrip() for x in open('day17test.txt', 'r')]
clay = []

dirs = [np.array([0,1]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1])]

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
        for d in dirs[0:1]:
            new_loc = drop + d
            if new_loc[1] >= grid.shape[0]:
                grid[drop[1], drop[0]] = "|"
                found = True
                break
            if grid[new_loc[1], new_loc[0]] == ".":
                #grid[drop[1], drop[0]] = "|"
                possibilities.insert(0, new_loc)
                found = True
                break
            if grid[new_loc[1], new_loc[0]] == "|":
                found = True
                #grid[drop[1], drop[0]] = "|"
                possibilities.append(new_loc)
                break

        if not found:
            for d in dirs[1:3]:
                new_loc = drop + d
                if new_loc[1] >= grid.shape[0]:
                    grid[drop[1], drop[0]] = "|"
                    found = True
                    break
                if grid[new_loc[1], new_loc[0]] == ".":
                    #grid[drop[1], drop[0]] = "|"
                    possibilities.insert(0, new_loc)
                    found = True
                    #break
                if grid[new_loc[1], new_loc[0]] == "|":
                    found = True
                    #grid[drop[1], drop[0]] = "|"
                    possibilities.append(new_loc)
                    #break
        if found and len(possibilities) > 0:
            grid[drop[1], drop[0]] = "|"
            new_loc = possibilities[0]
            next_water.append(new_loc)
            grid[new_loc[1], new_loc[0]] = "~"

        if not found:
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
        if a1[0] > a2[0]:
            return True
        elif a1[0] <= a2[0]:
            return False
    else:
        return False


water = []
last_tildes = -1
last_bars = -1
count = 0
while True:
    count += 1
    next_water = step(water)
    next_water.append(np.array([500, 0]))
    grid[0, 500] = "~"
    if np.array_equal(water, next_water):
        break
    water = sorted(next_water, key=functools.cmp_to_key(compare))
    if count % 100 == 0:
        print(count)

tildes = (grid[0:max_y+1, min_x:max_x+1] == "~").sum()
bars = (grid[0:max_y+1, min_x:max_x+1] == "|").sum()
print(tildes, bars)

with open('out.txt', "w") as f:
    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x + 1):
            print(grid[j, i], end="", file=f)
        print("", file=f)
print((grid[min_y:max_y+1, min_x:max_x+1] == "~").sum() + (grid[min_y:max_y+1, min_x:max_x+1] == "|").sum())