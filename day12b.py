#!/usr/bin/env python

class node:
    def __init__(self, n, nodes):
        self.n = n
        self.nodes = nodes

def connected_to(n, k, checked):
    global nodes
    checked.add(n)
    if k in nodes[n]:
        return True
    retval = False
    for nobe in nodes[n]:
        if nobe not in checked and connected_to(nobe, k, checked):
            return True
    return False

        

nodes = {}

for line in [x.rstrip().split() for x in open('day12input.txt', 'r').readlines()]:
    n = int(line[0])
    others = [int(x.rstrip(',')) for x in line[2:]]
    nodes[n] = others

count = 0
canonical_group_ids = set([0])
for i in nodes.keys():
    found_a_thing = False
    for j in canonical_group_ids:
        if connected_to(i, j, set()):
            print i, " is connected to ", j
            found_a_thing = True
            break
    if not found_a_thing:
        canonical_group_ids.add(i)


print len(canonical_group_ids)
