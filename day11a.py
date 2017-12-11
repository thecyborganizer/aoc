#!/usr/bin/env pc[1]thon
def n(c):
    return c[0], c[1]+1
def s(c):
    return c[0], c[1]-1
def ne(c):
    if c[0] % 2 == 0:
        return c[0]+1, c[1]+1
    else:
        return c[0]+1, c[1]
def se(c):
    if c[0] % 2 == 0:
        return c[0]+1, c[1]
    else:
        return c[0]+1, c[1]-1
def nw(c):
    if c[0] % 2 == 0:
        return c[0] - 1, c[1] + 1
    else:
        return c[0] - 1, c[1]
def sw(c):
    if c[0] % 2 == 0:
        return c[0] - 1, c[1]
    else:
        return c[0] - 1, c[1] - 1

def go_to_origin(c):
    pos = c
    count = 0
    while pos != (0,0):
        if pos[0] == 0:
            if pos[1] > 0:
                pos = s(pos)
            else:
                pos = n(pos)
        elif pos[0] > 0:
            if pos[1] >= 0:
                pos = sw(pos)
            else:
                pos = nw(pos)
        elif pos[0] < 0:
            if pos[1] >= 0:
                pos = se(pos)
            else:
                pos = ne(pos)
        count = count + 1
    return count

#c = sw(sw(se(sw(se((0,0))))))
#print go_to_origin(c)

string = open('day11input.txt', 'r').readline().rstrip().split(',')
c = (0,0)
m = 0
for d in string:
    if d == 'n':
        c = n(c)
    elif d == 'ne':
        c = ne(c)
    elif d == 'se':
        c = se(c)
    elif d == 's':
        c = s(c)
    elif d == 'sw':
        c = sw(c)
    elif d == 'nw':
        c = nw(c)
    else:
        print "Bad input: ", c
    if go_to_origin(c) > m:
        m = go_to_origin(c)

print go_to_origin(c)
print m
