#!/usr/bin/env python
memory = [int(x.rstrip()) for x in open('day5input.txt', 'r').readlines()]

#memory = [0,3,0,1,-3]
def evaluate(m, i):
    toreturn = i + m[i]
    if m[i] >= 3:
        m[i] = m[i] - 1
    else:
        m[i] = m[i] + 1
    return toreturn

index = 0
count = 0
while index >= 0 and index < len(memory):
    index = evaluate(memory, index)
#    print index, memory
    count = count + 1

print count
