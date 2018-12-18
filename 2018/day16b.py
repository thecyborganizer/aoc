import re

rs = [0]*4

opcode_list = ["eqrr", "eqri", "eqir", "gtrr", "gtri", "gtir", "setr", "seti", "borr", "bori", "banr", "bani", "mulr", "muli", "addr", "addi"]

opcodes = {}

def apply_instruction(instr, opcodes):
    global rs
    op, A, B, C = opcodes[instr[0]], instr[1], instr[2], instr[3]
    if op == "addr":
        rs[C] = rs[A] + rs[B]
    elif op == "addi":
        rs[C] = rs[A] + B
    elif op == "mulr":
        rs[C] = rs[A] * rs[B]
    elif op == "muli":
        rs[C] = rs[A] * B
    elif op == "banr":
        rs[C] = rs[A] & rs[B]
    elif op == "bani":
        rs[C] = rs[A] & B
    elif op == "borr":
        rs[C] = rs[A] | rs[B]
    elif op == "bori":
        rs[C] = rs[A] | B
    elif op == "setr":
        rs[C] = rs[A]
    elif op == "seti":
        rs[C] = A
    elif op == "gtir":
        if A > rs[B]:
            rs[C] = 1
        else:
            rs[C] = 0
    elif op == "gtri":
        if rs[A] > B:
            rs[C] = 1
        else:
            rs[C] = 0
    elif op == "gtrr":
        if rs[A] > rs[B]:
            rs[C] = 1
        else:
            rs[C] = 0
    elif op == "eqir":
        if A == rs[B]:
            rs[C] = 1
        else:
            rs[C] = 0
    elif op == "eqri":
        if rs[A] == B:
            rs[C] = 1
        else:
            rs[C] = 0
    elif op == "eqrr":
        if rs[A] == rs[B]:
            rs[C] = 1
        else:
            rs[C] = 0


def process_set(lines):
    global opcodes
    global opcode_list
    possibilities = set()
    start_state = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[0])))
    end_state = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[2])))
    instruction = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[1])))
    opcode, A, B, C = instruction[0], instruction[1], instruction[2], instruction[3]
    #print(start_state)
    #print(end_state)
    #print(opcode, A, B, C)
    if start_state[0:C] == end_state[0:C] and start_state[C+1:] == end_state[C+1:]:
        if (start_state[A] == start_state[B] and end_state[C] == 1) or (start_state[A] != start_state[B] and end_state[C] == 0):
            possibilities.add("eqrr")
        if (start_state[A] == B and end_state[C] == 1) or (start_state[A] != B and end_state[C] == 0):
            possibilities.add("eqri")
        if (A == start_state[B] and end_state[C] == 1) or (A != start_state[B] and end_state[C] == 0):
            possibilities.add("eqir")
        if (start_state[A] > start_state[B] and end_state[C] == 1) or (start_state[A] <= start_state[B] and end_state[C] == 0):
            possibilities.add("gtrr")
        if (start_state[A] > B and end_state[C] == 1) or (start_state[A] <= B and end_state[C] == 0):
            possibilities.add("gtri")
        if (A > start_state[B] and end_state[C] == 1) or (A <= start_state[B] and end_state[C] == 0):
            possibilities.add("gtir")
        if (end_state[C] == start_state[A]):
            possibilities.add("setr")
        if (end_state[C] == A):
            possibilities.add("seti")
        if (end_state[C] == start_state[A] | start_state[B]):
            possibilities.add("borr")
        if end_state[C] == start_state[A] | B:
            possibilities.add("bori")
        if end_state[C] == start_state[A] & start_state[B]:
            possibilities.add("banr")
        if end_state[C] == start_state[A] & B:
            possibilities.add("bani")
        if end_state[C] == start_state[A] * start_state[B]:
            possibilities.add("mulr")
        if end_state[C] == start_state[A] * B:
            possibilities.add("muli")
        if end_state[C] == start_state[A] + start_state[B]:
            possibilities.add("addr")
        if end_state[C] == start_state[A] + B:
            possibilities.add("addi")
    for o in possibilities:
        opcodes[o].add(opcode)
    
    return possibilities
text = [x.strip() for x in open('day16input1.txt', 'r')]
instructions = [list(map(lambda y: int(y), re.findall(r'-?\d+', x))) for x in open('day16input2.txt', 'r')]
for opcode in opcode_list:
    opcodes[opcode] = set()

#total = 0
for i in range(0, len(text), 4):
    possibilities = process_set(text[i:i+4])
    #if len(possibilities) >= 3:
        #total += 1
print(opcodes)

opcode_solutions = [""]*16

while len(opcodes.keys()) > 0:
    solo_key = ""
    for opcode in opcodes.keys():
        if len(opcodes[opcode]) == 1:
            solo_key = opcode            
            break
    solo_val = list(opcodes[solo_key])[0]
    opcode_solutions[solo_val] = solo_key
    del opcodes[solo_key]
    for opcode in opcodes.keys():
        if solo_val in opcodes[opcode]:
            opcodes[opcode].remove(solo_val)
#print(opcode_solutions)
#print(opcodes)
for i in instructions:
    apply_instruction(i, opcode_solutions)
    
print(rs)