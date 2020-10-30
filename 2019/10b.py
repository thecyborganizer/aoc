import math

space = []

def print_space(to_vape):
    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x]:
                if (x, y) == (station_x, station_y):
                    print("X", end="")
                elif (x, y) in to_vape:
                    print("*", end="")
                else:
                    print("#", end="")
            else:
                print(".", end="")
        print("")

def has_los(a, b):
    ax, ay, bx, by = 0,0,0,0

    if a[1] == b[1]:
        if a[0] > b[0]:
            ax, ay = b[1], b[0]
            bx, by = a[1], a[0]
        else:
            ax, ay = a[1], a[0]
            bx, by = b[1], b[0]
        for i in range(1, by - ay):
            if space[ay+i][ax]:
                return False
        return True
    if a[1] > b[1]:
        ax, ay = b[1], b[0]
        bx, by = a[1], a[0]
    else:
        ax, ay = a[1], a[0]
        bx, by = b[1], b[0]

    slope = (by - ay) / (bx - ax)
    for i in range(1, bx - ax):
        x = ax + i
        y = ay + (slope * i)
        if y.is_integer() and space[int(y)][x]:
            return False
    return True

with open("10input.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]
    for l in lines:
        row = []
        for c in l:
            if c == "#":
                row.append(True)
            else:
                row.append(False)
        space.append(row)

station_x, station_y = 20, 19

space_x = len(space[0])
space_y = len(space)

d = {}
for y in range(space_y):
    for x in range(space_x):
        if (x, y) == (station_x, station_y):
            continue
        angle = 0.0
        if x == station_x:
            if y < station_y:
                angle = 0.0
            else:
                angle = 180.0
        else:
            if (x > station_x) and (y < station_y):
                angle = 90 - math.degrees(math.atan((station_y - y) / (x - station_x)))
            elif (x > station_x) and (y >= station_y):
                angle = 90 + math.degrees(math.atan((y - station_y) / (x - station_x)))
            elif (x < station_x) and (y >= station_y):
                angle = 270 - math.degrees(math.atan((y - station_y) / (station_x - x)))
            else:
                angle = 270 + math.degrees(math.atan((station_y - y)/(station_x - x)))
        d[(x,y)] = angle

vaped = []
while len(vaped) < 202:
    to_vape = []
    for k, v in sorted(d.items(), key=lambda item: item[1]):
        if space[k[1]][k[0]] and has_los((station_y, station_x), (k[1], k[0])):
            to_vape.append(k)
    for v in to_vape:
        space[v[1]][v[0]] = False
        vaped.append(v)

vape_200 = vaped[199]
print(vape_200[0] * 100 + vape_200[1])
