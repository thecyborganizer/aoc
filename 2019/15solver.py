import re
import operator

with open("maze.txt") as f:
    walls = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])
    space = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])
    solution = set([tuple(map(lambda x: int(x), x.rstrip(')').lstrip('(').split(', '))) for x in re.findall("\(-?\d+, -?\d+\)", f.readline())])

queue = []

loc = (0,0)
queue.append(loc)
moves = [(0,1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W

seen = set()
prev = {}

while loc not in solution:
    #print(loc)
    loc = queue.pop(0)
    seen.add(loc)
    if loc in solution:
        #print(loc)
        break
    elif loc in space:
        for m in moves:
            new_loc = tuple(map(operator.add, loc, m))
            if new_loc not in seen:
                queue.append(new_loc)
                prev[new_loc] = loc

path = []
while loc != (0,0):
    path.append(loc)
    loc = prev[loc]

print(path)
print(len(path))