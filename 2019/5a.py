original_program = []

with open("5input.txt") as f:
#with open("5test.txt") as f:
    original_program = [int(x) for x in f.readline().rstrip().split(",")]
#original_program = program.copy()

def parse_opcode(opcode):
    o = list(str(opcode).zfill(5))
    instr = int("".join(o[4:]))
    mode1 = (int(o[2])) == 0
    mode2 = int(o[1]) == 0
    mode3 = int(o[0]) == 0
    return (instr, mode1, mode2, mode3)

def run_program(program):
    pc = 0

    while program[pc] != 99:
        (instr, mode1, mode2, mode3) = parse_opcode(program[pc])
        if instr == 1:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            program[op3] = (program[op2] if mode2 else op2) + (program[op1] if mode1 else op1)
            pc += 4
        elif instr == 2:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            program[op3] = (program[op2] if mode2 else op2) * (program[op1] if mode1 else op1)
            pc += 4
        elif instr == 3:
            op1 = program[pc + 1]
            val = int(input())
            program[op1] = val
            pc += 2
        elif instr == 4:
            op1 = program[pc + 1]
            print(program[op1] if mode1 else op1)
            pc += 2
        elif instr == 5:
            op2, op1 = (program[pc+2], program[pc+1])
            val2 = program[op2] if mode2 else op2
            val1 = program[op1] if mode1 else op1
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif instr == 6:
            op2, op1 = (program[pc+2], program[pc+1])
            val2 = program[op2] if mode2 else op2
            val1 = program[op1] if mode1 else op1
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif instr == 7:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            truth = (program[op2] if mode2 else op2) > (program[op1] if mode1 else op1)
            program[op3] = 1 if truth else 0
            pc += 4
        elif instr == 8:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            truth = (program[op2] if mode2 else op2) == (program[op1] if mode1 else op1)
            program[op3] = 1 if truth else 0
            pc += 4



    return program[0]

#print(program)
run_program(original_program)
#print(program)