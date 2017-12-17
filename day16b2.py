#!/usr/bin/env python

start_str = list("abcdefghijklmnop")
end_str = list("dcmlhejnifpokgba")

swaps = []

for c in list(map(chr, range(97, 97+16))):
    swaps.append(end_str.index(c))

def permute(string):
    global swaps
    l = [None] * 16
    i = 0
    for j in swaps:
        l[j] = string[i]
        i += 1
    return l

string = start_str
for i in xrange(9):
    if i % 500000 == 0:
        print i
    string = permute(string)
#    print string

#print "".join(string)

