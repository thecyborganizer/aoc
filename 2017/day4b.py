#!/usr/bin/env python

l = open('day4input.txt', 'r').readlines()
count=len(l)
for phrase in l:
    d = set()
    for word in phrase.split():
        sword = ''.join(sorted(word))
        if sword in d:
            count = count - 1
            break
        else:
            d.add(sword)

print count

