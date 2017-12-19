#!/usr/bin/env python

maze = [list(x) for x in open('day19input.txt', 'r').readlines()]

print maze[0]

pos = (0,0)

direction = 's'

seen = []
steps = 0

for i in range(len(maze[0])):
    if maze[0][i] == '|':
        pos = (0,i)

def move():
    global direction
    global pos
    global seen
    global steps
    c = maze[pos[0]][pos[1]]

    if c != '+' and c != '-' and c != '|':
        seen.append(c)

    if direction == 's':
        pos = (pos[0] + 1, pos[1])
    elif direction == 'w':
        pos = (pos[0], pos[1] - 1)
    elif direction == 'n':
        pos = (pos[0] - 1, pos[1])
    elif direction == 'e':
        pos = (pos[0], pos[1] + 1)
    steps += 1

def turn():
    global direction
    global pos
    global maze
    hits = []
    if maze[pos[0]-1][pos[1]] != ' ':
        hits.append('n')
    if maze[pos[0]][pos[1] + 1] != ' ':
        hits.append('e')
    if maze[pos[0]+1][pos[1]] != ' ':
        hits.append('s')
    if maze[pos[0]][pos[1] - 1] != ' ':
        hits.append('w')
    if direction == 'n':
        hits.remove('s')
    elif direction == 'e':
        hits.remove('w')
    elif direction == 's':
        hits.remove('n')
    elif direction == 'w':
        hits.remove('e')
    direction = hits[0] 

def evaluate():
    global pos
    global maze
    global direction
    print pos
    c = maze[pos[0]][pos[1]]
    if c == '-' or c == '|':
        move()
    elif c == '+':
        turn()
        move()
    elif c == ' ':
        print "ERROR"
        return True
    else:
        move()
    return False

while True:
    if evaluate():
        break

print "".join(seen)

print steps
