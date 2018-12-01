#!/usr/bin/env python


txt = [x.split(':') for x in open('day13input.txt', 'r').readlines()]
layers = {}
for t in txt:
    layers[int(t[0])] = (0,int(t[1].strip()), False)

def update_layers(layers):
    for k in layers.keys():
        v = layers[k]
        if v[2]:
            layers[k] = (v[0] - 1, v[1], (v[0] - 1 != 0))
        else:
            layers[k] = (v[0] + 1, v[1], (v[0] + 1 == v[1] - 1))


depth = 0
severity = 0
m = max(layers.keys())
while depth <= m:
    if depth in layers.keys():
        if layers[depth][0] == 0:
            print "Hit at depth ", depth, " severity is ", depth * layers[depth][1]
            severity = severity + depth * layers[depth][1]
    depth = depth + 1
    update_layers(layers)

print severity
