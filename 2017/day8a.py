#!/usr/bin/env python

import operator

instructions = open('day8input.txt', 'r').readlines()

registers = {}

def evaluate(r0, lval, op, r1, rval, comp, rs):
    opfunc = operator.add
    if op == "dec":
        opfunc = operator.sub
    cmpfunc = operator.gt
    if comp == "<":
        cmpfunc = operator.lt
    elif comp == "<=":
        cmpfunc = operator.le
    elif comp == ">=":
        cmpfunc = operator.ge
    elif comp == "==":
        cmpfunc = operator.eq
    elif comp == "!=":
        cmpfunc = operator.ne

    if cmpfunc(rs[r1], rval):
        rs[r0] = opfunc(rs[r0], lval)

maximum = 0
for inst in instructions:
    sinst = inst.split()
    r0 = sinst[0]
    op = sinst[1]
    lval = int(sinst[2])
    r1 = sinst[4]
    comp = sinst[5]
    rval = int(sinst[6])
    if r0 not in registers.keys():
        registers[r0] = 0
    if r1 not in registers.keys():
        registers[r1] = 0
    evaluate(r0, lval, op, r1, rval, comp, registers)
    if max(registers.values()) > maximum:
        maximum = max(registers.values())

print max(registers.values())
print maximum
