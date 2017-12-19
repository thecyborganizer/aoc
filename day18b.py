#!/usr/bin/env python

memory = [x.rstrip().split() for x in open('day18input.txt', 'r').readlines()]

class compy:
    def __init__(self, pid):
        self.pc = 0
        self.pid = pid
        self.registers={}
        self.memory = [x.rstrip().split() for x in open('day18input.txt', 'r').readlines()]
        self.queue = []
        self.waiting = False
        self.done = False
        self.times_sent = 0
        for i in range(97, 97+26):
            self.registers[chr(i)] = 0
        self.registers['p'] = pid

compys = [compy(0), compy(1)]

def eval_arg(arg, compy):
    retval = 0
    try:
        retval = int(arg)
    except ValueError:
        retval = compy.registers[arg]
    return retval

def run_inst(compy):
    global compys
    if compy.pc >= len(compy.memory) or compy.pc < 0:
        compy.done = True
        return
    inst = compy.memory[compy.pc]
#    print inst
    op = inst[0]
    o1 = inst[1]
    o2 = 0
    if len(inst) > 2:
        o2 = inst[2]
     
#    print eval_arg(o1), eval_arg(o2)
    if op == 'snd':
        if compy.pid == 0:
            compys[1].queue.append(eval_arg(o1, compy))
        else:
            compy.times_sent += 1
            compys[0].queue.append(eval_arg(o1, compy))
    elif op == 'set':
        compy.registers[o1] = eval_arg(o2, compy)
    elif op == 'add':
        compy.registers[o1] += eval_arg(o2, compy)
    elif op == 'mul':
        compy.registers[o1] = compy.registers[o1] * eval_arg(o2, compy)
    elif op == 'mod':
        compy.registers[o1] = compy.registers[o1] % eval_arg(o2, compy)
    elif op == 'rcv':
        if len(compy.queue) > 0:
            compy.waiting = False
            compy.registers[o1] = compy.queue.pop(0)
        else:
            compy.waiting = True
    elif op == 'jgz':
        if eval_arg(o1, compy) > 0:
            compy.pc += eval_arg(o2, compy)
        else:
            compy.pc += 1

    if op != 'jgz' and not compy.waiting:
        compy.pc += 1


while not ((compys[0].waiting or compys[0].done) and (compys[1].waiting or compys[1].done)):
    run_inst(compys[0])
    run_inst(compys[1])

print compys[1].times_sent
