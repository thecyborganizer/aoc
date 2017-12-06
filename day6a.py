#!/usr/bin/env python

def redistribute(m):
    i = m.index(max(m))
    count = m[i]
    m[i] = 0
    while count > 0:
        i = (i + 1) % len(m)
        m[i] = m[i] + 1
        count = count - 1
    

memstr = "2   8   8   5   4   2   3   1   5   5   1   2   15  13  5   14"
memory = [int(x) for x in memstr.split()]

states = set()
d = {}
count = 0
while tuple(memory) not in states:
    states.add(tuple(memory))
    d[tuple(memory)] = count
    redistribute(memory)
    count = count + 1

#part a
print count
#part b
print count - d[tuple(memory)]
