#!/usr/bin/env python

#with open('day2input.txt', 'r') as f:
#    listoflistofstrings = [x.split() for x in f.readlines()]
#    listoflistofints = [[int(y) for y in l] for l in [x.split() for x in f.readlines()]]h
print sum([max(k) - min(k) for k in [[int(y) for y in l] for l in [x.split() for x in open('day2input.txt', 'r').readlines()]]])
#    total = sum(listofdiffs)
    #l = [max(y) - min(y) for y in [int([x.split() for x in f.readlines()])[i]for i in range(len(]]




