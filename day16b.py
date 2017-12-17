#!/usr/bin/env python

cmds = open('day16input.txt', 'r').readline().rstrip().split(',')
chars = list(map(chr, range(97, 97+16)))
cmd_list = []
def build_cmd_list(cmds):
    global cmd_list
    for cmd in cmds:
        if cmd[0] == 's':
            val = int(cmd.lstrip('s'))
            cmd_list.append(('s', val))
        elif cmd[0] == 'x':
            lval = int(cmd[1:].split('/')[0])
            rval = int(cmd[1:].split('/')[1])
            cmd_list.append(('x', lval, rval))
        elif cmd[0] == 'p':
            lchar = cmd[1:].split('/')[0]
            rchar = cmd[1:].split('/')[1]
            cmd_list.append(('p', lchar, rchar))

def evaluate(cmd):
    global chars
    if cmd[0] == 's':
        val = cmd[1]
        to_move = chars[-val:]
        chars = to_move + chars[:-val]
    elif cmd[0] == 'x':
        lval = cmd[1]
        rval = cmd[2]
        tmp = chars[lval]
        chars[lval] = chars[rval]
        chars[rval] = tmp
    elif cmd[0] == 'p':
        lchar = cmd[1]
        rchar = cmd[2]
        lindex = chars.index(lchar)
        rindex = chars.index(rchar)
        tmp = chars[lindex]
        chars[lindex] = chars[rindex]
        chars[rindex] = tmp

#for i in xrange(1000000000):
build_cmd_list(cmds)
seen = set()
seen.add("".join(chars))
for i in xrange(1000000000):
    for c in cmd_list:
        evaluate(c)
    string = "".join(chars)
    if string in seen:
        print i, string
    else:
        seen.add(string)

#print "".join(chars)
