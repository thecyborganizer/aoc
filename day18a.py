#!/usr/bin/env python

memory = [x.rstrip().split() for x in open('day18input.txt', 'r').readlines()]

pc = 0
registers = {}
for i in range(97, 97 + 26):
    registers[chr(i)] = 0

last_sound = 0

def eval_arg(arg):
    global registers
    retval = 0
    try:
        retval = int(arg)
    except ValueError:
        retval = registers[arg]
    return retval


while pc >= 0 and pc < len(memory):
    inst = memory[pc]
#    print inst
    op = inst[0]
    o1 = inst[1]
    o2 = 0
    if len(inst) > 2:
        o2 = inst[2]
    
#    print eval_arg(o1), eval_arg(o2)
    if op == 'snd':
        last_sound = eval_arg(o1)
    elif op == 'set':
        registers[o1] = eval_arg(o2)
    elif op == 'add':
        registers[o1] += eval_arg(o2)
    elif op == 'mul':
        registers[o1] = registers[o1] * eval_arg(o2)
    elif op == 'mod':
        registers[o1] = registers[o1] % eval_arg(o2)
    elif op == 'rcv':
        if last_sound != 0:
            registers[o1] = last_sound
            print last_sound
    elif op == 'jgz':
        if eval_arg(o1) > 0:
            pc += eval_arg(o2)
        else:
            pc += 1

    if op != 'jgz':
        pc += 1


