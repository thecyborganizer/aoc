#!/usr/bin/env python

class threevec:
    def __init__(self, t):
        self.x = int(t[0])
        self.y = int(t[1])
        self.z = int(t[2])

class particle:
    def __init__(self, pid, p, v, a):
        self.pid = pid
        self.p = threevec(p)
        self.v = threevec(v)
        self.a = threevec(a)


def update(r):
    r.v.x += r.a.x
    r.v.y += r.a.y
    r.v.z += r.a.z
    r.p.x += r.v.x
    r.p.y += r.v.y
    r.p.z += r.v.z
    return r

def distance(r):
    return abs(r.p.x) + abs(r.p.y) + abs(r.p.z)

def amag(r):
    return abs(r.a.x) + abs(r.a.y) + abs(r.a.z)

i = [x.split() for x in open('day20input.txt', 'r').readlines()]

particles = []
count = 0
for row in i:
    r = [k.rstrip(',') for k in row]
    p = particle(count, r[0].lstrip('p=<').rstrip('>').split(','), r[1].lstrip('v=<').rstrip('>').split(','), r[2].lstrip('a=<').rstrip('>').split(','))
    particles.append(p)
    count += 1

amags = map(amag, particles)

print amags.index(min(amags))
