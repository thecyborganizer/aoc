#!/usr/bin/env python

cmds = open('day16input.txt', 'r').readline().rstrip().split(',')
chars = list(map(chr, range(97, 97+16)))

def evaluate(cmd):
    global chars
    if cmd[0] == 's':
        val = int(cmd.lstrip('s'))
        to_move = chars[-val:]
        chars = to_move + chars[:-val]
    elif cmd[0] == 'x':
        lval = int(cmd[1:].split('/')[0])
        rval = int(cmd[1:].split('/')[1])
        tmp = chars[lval]
        chars[lval] = chars[rval]
        chars[rval] = tmp
    elif cmd[0] == 'p':
        lchar = cmd[1:].split('/')[0]
        rchar = cmd[1:].split('/')[1]
        lindex = chars.index(lchar)
        rindex = chars.index(rchar)
        tmp = chars[lindex]
        chars[lindex] = chars[rindex]
        chars[rindex] = tmp
    else:
        print "bad command!"


for c in cmds:
    evaluate(c)
    print chars

print "".join(chars)
