#!/usr/bin/env python
import time 
stream = list(open('day9input.txt', 'r').readline().rstrip())

total_score = 0
garbage_chars = 0



def consume_garbage(s, i):
    global garbage_chars
    ignore_next = False
    while i < len(s):
        c = s[i]
        i = i + 1
        if ignore_next:
            ignore_next = False
            continue
        if c == '!':
            ignore_next = True
            continue
        if c == '>':
            return i
        garbage_chars += 1


def score_group(s, i, outer_score):
    global total_score
    score = outer_score + 1
    while i < len(s):
        c = s[i]
        i = i + 1
        if c == '<':
            i = i + consume_garbage(s[i:], 0)
        elif c == '{':
            offset = score_group(s[i:], 0, score)
            i = i + offset
        elif c == '}':
            total_score = total_score + score
            return i


score_group(stream, 1, 0)
#s = list("{o\"i!a,<{i<a>")
#consume_garbage(s,0)

print total_score
print garbage_chars
