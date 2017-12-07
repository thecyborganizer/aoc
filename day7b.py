#!/usr/bin/env python

class node:
    def __init__(self, name, weight, children):
        self.name=name
        self.weight=weight
        self.children=children

def build_node(name, d):
    n = node(name, d[name][0], [])
    if len(d[name][1]) == 0:
        return n
    else:
        for s in d[name][1]:
            n.children.append(build_node(s,d))
        return n

def stack_weight(n):
    if len(n.children) == 0:
        return n.weight
    else:
        weight = n.weight
        for c in n.children:
            weight = weight + stack_weight(c)
        return weight

node_data = {}

for l in open('day7input.txt', 'r').readlines():
    ll = l.split()
    name = ll[0]
    weight = int(ll[1].lstrip('(').rstrip(')'))
    children = []
    if len(ll) > 2:
        for n in ll[3:]:
            children.append(n.rstrip(", "))
    node_data[name] = (weight, children)

root = build_node("vmpywg", node_data)

n = root
while True:
    weights = []
    for c in n.children:
        weights.append(stack_weight(c))
    print weights
    if max(weights) != min(weights):
        i = weights.index(max(weights))
        n = n.children[i]
        if len(n.children) == 0:
            print n.name
            break
        else:
            continue
    else:
        print n.name
        break
