def moveTail(headPos, tailPos):
    (headX, headY) = headPos
    (tailX, tailY) = tailPos
    if abs(headX - tailX) <= 1 and abs(headY - tailY) <= 1:
        return tailPos
    if (tailY == headY):
        if headX > tailX:
            return (tailX + 1, tailY)
        else:
            return (tailX - 1, tailY)
    elif (tailX == headX):
        if headY > tailY:
            return (tailX, tailY + 1)
        else:
            return (tailX, tailY - 1)
    else:
        if (headX > tailX and headY > tailY):
            return (tailX + 1, tailY + 1)
        elif (headX > tailX and headY < tailY):
            return (tailX + 1, tailY - 1)
        elif (headX < tailX and headY > tailY):
            return (tailX - 1, tailY + 1)
        elif (headX < tailX and headY < tailY):
            return (tailX - 1, tailY - 1)

instructions = []
with open("day9input.txt") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]

headPos = (0, 0)
tailPos = (0, 0)
knots = [(0, 0) for _ in range(9)]
visits = set()
knotVisits = set()
for i in instructions:
    [direction, count] = i[:2]
    #print(i)
    for j in range(int(count)):
        #print(direction)
        if direction == "R":
            headPos = (headPos[0] + 1, headPos[1])
        elif direction == "L":
            headPos = (headPos[0] - 1, headPos[1])
        elif direction == "U":
            headPos = (headPos[0], headPos[1] + 1)
        else:
            headPos = (headPos[0], headPos[1] - 1)
        tailPos = moveTail(headPos, tailPos)
        visits.add(tailPos)

        knots[0] = moveTail(headPos, knots[0])
        for i in range(1, len(knots)):
            knots[i] = moveTail(knots[i-1], knots[i])
        knotVisits.add(knots[-1])
print(len(visits))
print(len(knotVisits))
