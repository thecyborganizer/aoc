#!/usr/bin/env python

f = open('day1input.txt', 'r')
s = list(f.read().rstrip())

total = 0
for c in range(len(s)):
    if s[c] == s[(c+(len(s)/2)) % len(s)]:
        total += int(s[c])

print total
