import re

rs = [0]*4

def process_set(lines):
    possibilities = []
    start_state = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[0])))
    end_state = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[2])))
    instruction = list(map(lambda x: int(x), re.findall(r'-?\d+', lines[1])))
    opcode, A, B, C = instruction[0], instruction[1], instruction[2], instruction[3]
    #print(start_state)
    #print(end_state)
    #print(opcode, A, B, C)
    if start_state[0:C] == end_state[0:C] and start_state[C+1:] == end_state[C+1:]:
        if (start_state[A] == start_state[B] and end_state[C] == 1) or (start_state[A] != start_state[B] and end_state[C] == 0):
            possibilities.append("eqrr")
        if (start_state[A] == B and end_state[C] == 1) or (start_state[A] != B and end_state[C] == 0):
            possibilities.append("eqri")
        if (A == start_state[B] and end_state[C] == 1) or (A != start_state[B] and end_state[C] == 0):
            possibilities.append("eqir")
        if (start_state[A] > start_state[B] and end_state[C] == 1) or (start_state[A] <= start_state[B] and end_state[C] == 0):
            possibilities.append("gtrr")
        if (start_state[A] > B and end_state[C] == 1) or (start_state[A] <= B and end_state[C] == 0):
            possibilities.append("gtri")
        if (A > start_state[B] and end_state[C] == 1) or (A <= start_state[B] and end_state[C] == 0):
            possibilities.append("gtir")
        if (end_state[C] == start_state[A]):
            possibilities.append("setr")
        if (end_state[C] == A):
            possibilities.append("seti")
        if (end_state[C] == start_state[A] | start_state[B]):
            possibilities.append("borr")
        if end_state[C] == start_state[A] | B:
            possibilities.append("bori")
        if end_state[C] == start_state[A] & start_state[B]:
            possibilities.append("banr")
        if end_state[C] == start_state[A] & B:
            possibilities.append("bani")
        if end_state[C] == start_state[A] * start_state[B]:
            possibilities.append("mulr")
        if end_state[C] == start_state[A] * B:
            possibilities.append("muli")
        if end_state[C] == start_state[A] + start_state[B]:
            possibilities.append("addr")
        if end_state[C] == start_state[A] + B:
            possibilities.append("addi")
    return possibilities
#text = ["Before: [3, 2, 1, 1]", "9 2 1 2", "After:  [3, 2, 2, 1]"]
text = [x.strip() for x in open('day16input1.txt', 'r')]
#process_set(text[0:4])
#process_set(text[4:8])
#print(process_set(text))
total = 0
for i in range(0, len(text), 4):
    possibilities = process_set(text[i:i+4])
    if len(possibilities) >= 3:
        total += 1
print(total)