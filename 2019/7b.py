import itertools

original_program = []

with open("7input.txt") as f:
#with open("7test.txt") as f:
    original_program = [int(x) for x in f.readline().rstrip().split(",")]
#original_program = program.copy()

def parse_opcode(opcode):
    o = list(str(opcode).zfill(5))
    instr = int("".join(o[4:]))
    mode1 = (int(o[2])) == 0
    mode2 = int(o[1]) == 0
    mode3 = int(o[0]) == 0
    return (instr, mode1, mode2, mode3)

def run_program(program, inputs, ip):
    pc = ip

    while True:
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
            #val = int(input())
            val = inputs.pop(0)
            program[op1] = val
            pc += 2
        elif instr == 4:
            op1 = program[pc + 1]
            #print(program[op1] if mode1 else op1)
            pc += 2
            return ((program[op1] if mode1 else op1), pc)

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
        elif instr == 9:
            return (True, 12345)
        else:
            print("Invalid opcode")
            #raise TypeError("um")
            return

phase_settings = list(itertools.permutations(range(9,4,-1)))
maximum = 0
best_settings = []

for p in phase_settings:
    programs = [original_program.copy() for i in range(5)]
    retvals = [0,0,0,0,0]
    complete = [False, False, False, False, False]
    first_time = [True, True, True, True, True]
    pcs = [0,0,0,0,0]
    input_val = 0
    i = 0
    while False in complete:
        inputs = []
        if first_time[i]:
            inputs = [p[i], input_val]
            first_time[i] = False
        else:
            inputs = [input_val]
        retval, pc = run_program(programs[i], inputs, pcs[i])
        if isinstance(retval, bool):
            complete[i] = True
            input_val = retvals[i]
        else:
            retvals[i] = retval
            input_val = retval
            pcs[i] = pc
        i = (i + 1) % 5
    if retvals[4] > maximum:
        maximum = retvals[4]
        best_settings = p

print(best_settings)
print(maximum)
#run_program(original_program)
