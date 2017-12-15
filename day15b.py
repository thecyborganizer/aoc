#!/usr/bin/env python

def generate(value, factor):
    return (value * factor) % 2147483647

def compare(a, b):
    return (a & 0xFFFF) == (b & 0xFFFF)

a = 65
b = 8921
#a = 289
#b = 629
count = 0
comparisons = 0
alist = []
blist = []
while comparisons < 5000000:
    if comparisons % 100000 == 0:
        print comparisons
    a = generate(a, 16807)
    b = generate(b, 48271)
    if (a % 4 == 0):
        alist.append(a)
    if (b % 8 == 0):
        blist.append(b)
    while len(alist) > 0 and len(blist) > 0:
        comparisons += 1
        if compare(alist.pop(0), blist.pop(0)):
            count += 1



print count
