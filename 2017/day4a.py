#!/usr/bin/env python

l = open('day4input.txt', 'r').readlines()
count=0
for phrase in l:
    d = set()
    for word in phrase.split():
        if word in d:
            count = count + 1
            break
        else:
            d.add(word)

#actually the inverse of this, oops
print count

