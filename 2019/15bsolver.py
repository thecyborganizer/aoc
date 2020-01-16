import re
import operator

with open("maze.txt") as f:
    walls = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])
    space = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])
    oxygen = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])

queue = []

loc = (0,0)
queue.append(loc)
moves = [(0,1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W

time = 0
while len(space) > 0:
    to_add = set()
    for s in oxygen:
        for m in moves:
            adjacent = tuple(map(operator.add, s, m))
            if adjacent in space:
                to_add.add(adjacent)
                space.remove(adjacent)
    oxygen = oxygen.union(to_add)
    time += 1

print(time)
