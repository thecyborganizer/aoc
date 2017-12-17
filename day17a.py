#!/usr/bin/env python

steps = 382
#steps = 3
spin = [0]
pos = 0
length = 1
val = 0
for i in xrange(1,50000001):
    pos = (pos + steps) % length + 1
    length += 1
    if pos == 1:
        print i
        val = i

print val
