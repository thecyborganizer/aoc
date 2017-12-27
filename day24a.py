#!/usr/bin/env python

connectors = map(lambda x : (int(x[0]), int(x[1])), [x.rstrip().split('/') for x in open('day24input.txt').readlines()])
#connectors = map(lambda x : (int(x[0]), int(x[1])), [x.rstrip().split('/') for x in open('day24test.txt').readlines()])

class bridge:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.connectors = []
        self.strength = 0

def add(br, connector):
    b = bridge()
    if br.right == connector[0]:
        b.right = connector[1]
    elif br.right == connector[1]:
        b.right = connector[0]
    b.connectors = list(br.connectors)
    b.connectors.append(connector)
    b.strength = br.strength + connector[0] + connector[1]
    return b

def fits(bridge, connector):
    return connector not in bridge.connectors and (bridge.right == connector[0] or bridge.right == connector[1])

bridges = []

for c in connectors:
    b = bridge()
    if fits(b, c):
        bridges.append(add(b, c))
for i in range(2, 50):
    print i
    to_append = []
    for b in bridges:
        for c in connectors:
            if fits(b, c):
                to_add = add(b, c)
                if len(to_add.connectors) >= i:
                    to_append.append(to_add)
    if len(to_append) == 0:
        break
    bridges = bridges + to_append

max_len = 0
max_str = 0
for b in bridges:
    if len(b.connectors) > max_len:
        max_len = len(b.connectors)
        max_str = b.strength
    elif len(b.connectors) == max_len:
        if b.strength > max_str:
            max_str = b.strength

print max_str

