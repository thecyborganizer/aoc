#!/usr/bin/env python


txt = [x.split(':') for x in open('day13input.txt', 'r').readlines()]
layers = {}
for t in txt:
    layers[int(t[0])] = int(t[1].strip())

def is_zero(l, t):
    global layers
    return l in layers.keys() and (t % ((layers[l] - 1) * 2)) == 0


def attempt(t):
    global layers
    depth = 0
    m = max(layers.keys())
    for i in range(m + 1):
        if is_zero(i, t):
            return False
        t += 1
    return True


delay = 0
while True:
    if delay % 1000 == 0:
        print delay
    if attempt(delay):
        break
    delay = delay + 1

print delay
