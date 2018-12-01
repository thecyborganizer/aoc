#!/usr/bin/env python

parents = []
children = []

for l in open('day7input.txt', 'r').readlines():
    ll = l.split()
    parents.append(ll[0])
    if len(ll) > 2:
        for n in ll[3:]:
            children.append(n.rstrip(", "))


for n in parents:
    if n not in children:
        print n
