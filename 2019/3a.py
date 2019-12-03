wires = []

with open("3input.txt") as f:
#with open("3test.txt") as f:
    wires.append([(list(x)[0], int("".join(list(x)[1:]))) for x in f.readline().rstrip().split(",")])
    wires.append([(list(x)[0], int("".join(list(x)[1:]))) for x in f.readline().rstrip().split(",")])

#print(wires)

wire_points = [set(), set()]
steps_to_get_there = [{}, {}]
for i in range(2):
    loc = (0,0)
    steps = 0
    for cmd in wires[i]:
        direction =  cmd[0]
        distance = cmd[1]
        for j in range(distance):
            steps += 1
            if direction == 'R':
                loc = (loc[0] + 1, loc[1])
            elif direction == 'L':
                loc = (loc[0] - 1, loc[1])
            elif direction == 'U':
                loc = (loc[0], loc[1] + 1)
            elif direction == 'D':
                loc = (loc[0], loc[1] - 1)
            wire_points[i].add(loc)
            if loc not in steps_to_get_there[i].keys(): 
                steps_to_get_there[i][loc] = steps

print(min([abs(x[0]) + abs(x[1]) for x in wire_points[0].intersection(wire_points[1])]))

distances = []
intersection = wire_points[0].intersection(wire_points[1])
for p in intersection:
    distances.append(steps_to_get_there[0][p] + steps_to_get_there[1][p])
distances.sort()
print(distances)