import sys

with open("day12input.txt") as f:
    map = [[int(ord(y)) - ord('a') for y in list(x.strip())] for x in f.readlines()]

S = (0, 0)
E = (0, 0)

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == ord('S') - ord('a'):
            map[y][x] = ord('a') - ord('a')
            S = (x, y)
        elif map[y][x] == ord('E') - ord('a'):
            map[y][x] = ord('z') - ord('a')
            E = (x, y)
def availableMoves(pos):
    global map
    (width, length) = len(map[0]), len(map)
    (x, y) = pos
    toReturn = []
    height = map[y][x]
    #north
    if y > 0 and height - map[y-1][x] <= 1:
        toReturn.append((x, y-1))
    #east
    if x < width - 1 and height - map[y][x+1] <= 1:
        toReturn.append((x+1, y))
    #south
    if y < length - 1 and height - map[y+1][x] <= 1:
        toReturn.append((x, y+1))
    #west
    if x > 0 and height - map[y][x-1] <= 1:
        toReturn.append((x-1, y))
    return toReturn
    
def generatePath(pos, destination):
    global prev
    path = []
    while pos != destination and pos in prev:
        path.append(pos)
        pos = prev[pos]
    return path

def printPath(pathSet):
    global map
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x, y) in pathSet:
                print("#", end="")
            else:
                print(chr(map[y][x]+ord('a')), end ="")
        print("")

pos = E
destination = S
unvisitedSet = set((x, y) for x in range(len(map[0])) for y in range(len(map)))
tentativeDistance = {}
prev = {}
for s in unvisitedSet:
    tentativeDistance[s] = sys.maxsize
tentativeDistance[pos] = 0
while(pos != destination):
    neighbors = availableMoves(pos)
    currentDistance = tentativeDistance[pos]
    for n in neighbors:
        distanceToNeighbor = currentDistance + 1
        tentativeNeighborDistance = tentativeDistance[n]
        if tentativeDistance[n] > distanceToNeighbor:
            tentativeDistance[n] = distanceToNeighbor
            prev[n] = pos
    unvisitedSet.remove(pos)
    if destination not in unvisitedSet:
        break
    minimumSoFar = sys.maxsize
    for u in unvisitedSet:
        if tentativeDistance[u] < minimumSoFar:
            pos = u
            minimumSoFar = tentativeDistance[u]

path = generatePath(S, E)
print("Part 1: {}".format(len(path)))
#print(path)

minSoFar = sys.maxsize
bestPath = []
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            path = generatePath((x,y), E)
            #print(path)
            if len(path) < minSoFar and len(path) > 0:
                minSoFar = len(path)
                bestPath = path
                print(bestPath)
print(minSoFar)
# actualBest = generatePath(destination, (0, 5))
# print(actualBest)
# printPath(set(actualBest))
