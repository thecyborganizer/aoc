import re
import operator

rs = [0]*6
ip_register = 4
opcode_list = ["eqrr", "eqri", "eqir", "gtrr", "gtri", "gtir", "setr", "seti", "borr", "bori", "banr", "bani", "mulr", "muli", "addr", "addi"]

opcodes = {}


def addr(a, b, rs):
    return rs[a] + rs[b]
def addi(a, b, rs):
    return rs[a] + b
def mulr(a,b,rs):
    return rs[a]*rs[b]
def muli(a,b,rs):
    return rs[a]*b
def banr(a,b,rs):
    return rs[a] & rs[b]
def bani(a,b,rs):
    return rs[a] & b
def borr(a,b,rs):
    return rs[a] | rs[b]
def bori(a,b,rs):
    return rs[a] | b
def setr(a,b,rs):
    return rs[a]
def seti(a,b,rs):
    return a
def gtir(a,b,rs):
    if a > rs[b]:
        return 1
    else:
        return 0
def gtri(a,b,rs):
    if rs[a] > b:
        return 1
    else:
        return 0
def gtrr(a,b,rs):
    if rs[a] > rs[b]:
        return 1
    else:
        return 0
def eqir(a,b,rs):
    if a == r[b]:
        return 1
    else:
        return 0
def eqri(a,b,rs):
    if rs[a] == b:
        return 1
    else:
        return 0
def eqrr(a,b,rs):
    if rs[a] == rs[b]:
        return 1
    else:
        return 0
opcode_dict = {"addr": addr, "addi": addi, "mulr": mulr, "muli": muli, "banr": banr, "bani": bani, "borr": borr, "bori": bori, "setr": setr, "seti": seti, "gtir": gtir, "gtri": gtri, "gtrr": gtrr, "eqir": eqir, "eqri": eqri, "eqrr": eqrr}

def apply_instruction(instr, rs):
    global opcode_dict
    op, A, B, C = instr[0], instr[1], instr[2], instr[3]
    f = opcode_dict[op]
    rs[C] = f(A, B, rs)

    
#program = [[x.split()[0]] + list(map(lambda y: int(y), re.findall(r'-?\d+', x))) for x in open('day19test.txt', 'r')]
program = [[x.split()[0]] + list(map(lambda y: int(y), re.findall(r'-?\d+', x))) for x in open('day19input.txt', 'r')]

ip = 0
count = 0
while ip >= 0 and ip < len(program):
    count += 1
    print(count, rs)
    rs[ip_register] = ip
    
    apply_instruction(program[rs[ip_register]], rs)
    ip = rs[ip_register] + 1

print(rs)
#for i in instructions:
#    apply_instruction(i, opcode_solutions)
    
#print(rs)