#!/usr/bin/env python

def generate(value, factor):
    return (value * factor) % 2147483647

def compare(a, b):
    return (a & 0xFFFF) == (b & 0xFFFF)

#a = 65
#b = 8921
a = 289
b = 629
count = 0
for i in xrange(40000000):
    if i % 1000000 == 0:
        print i
    a = generate(a, 16807)
    b = generate(b, 48271)
    if compare(a, b):
        count += 1

print count
