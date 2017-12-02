#!/usr/bin/env python

def evdivs(li):
    return [i/j for i in li for j in li if i % j == 0 and i != j][0]

print sum([evdivs(k) for k in [[int(y) for y in l] for l in [x.split() for x in open('day2input.txt', 'r').readlines()]]])
