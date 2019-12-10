space = []

with open("10input.txt") as f:
#with open("10test.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]
    for l in lines:
        row = []
        for c in l:
            if c == "#":
                row.append(True)
            else:
                row.append(False)
        space.append(row)

def print_space():
    for l in space:
        for c in l:
            if c:
                print("#", end="")
            else:
                print(".", end="")
        print("")

def has_los(a, b):
    ax, ay, bx, by = 0,0,0,0

    if a[0] > b[0]:
        ay, ax = b[1], b[0]
        by, bx = a[1], a[0]
    else:
        ay, ax = a[1], a[0]
        by, bx = b[1], b[0]

    if (ax == bx):
        for i in range(min(ay, by) + 1, max(ay, by)):
            if space[i][ax]:
                return False
        return True

    slope = (by - ay) / (bx - ax)

    for i in range(1, bx - ax):
        x = ax + i
        y = ay + (slope * i)
        if y.is_integer() and space[int(y)][x]:
            return False
    return True

print_space()

#print(has_los((3,4),(1,0)))
#print(has_los((3,4), (4,0)))
#print(has_los((4,4), (4,0)))

max_los = 0
coords = (-1, -1)
for ay in range(len(space)):
    for ax in range(len(space[0])):
        if space[ay][ax]:
            los_count = 0
            for by in range(len(space)):
                for bx in range(len(space[0])):
                    if (ax, ay) != (bx, by) and space[by][bx] and has_los((ax, ay), (bx, by)):
                        los_count += 1
            if los_count > max_los:
                max_los = max(los_count, max_los)
                coords = (ax, ay)
print(max_los)
print(coords)