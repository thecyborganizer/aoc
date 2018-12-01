#!/usr/bin/env python

class node:
    def __init__(self, n, nodes):
        self.n = n
        self.nodes = nodes

def connected_to_zero(n, checked):
    global nodes
    print "checking ", n
    checked.add(n)
    if 0 in nodes[n]:
        return True
    retval = False
    for nobe in nodes[n]:
        if nobe not in checked and connected_to_zero(nobe, checked):
            return True
    return False

        

nodes = {}

for line in [x.rstrip().split() for x in open('day12input.txt', 'r').readlines()]:
    n = int(line[0])
    others = [int(x.rstrip(',')) for x in line[2:]]
    nodes[n] = others

count = 0
for i in nodes.keys():
    if connected_to_zero(i, set()):
        count = count + 1

print count
