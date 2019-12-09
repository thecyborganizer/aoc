import itertools

original_program = []

with open("9input.txt") as f:
#with open("9test.txt") as f:
    original_program = [int(x) for x in f.readline().rstrip().split(",")]
#original_program = program.copy()

def parse_opcode(opcode):
    # o = list(str(opcode).zfill(5))
    # instr = int("".join(o[4:]))
    # mode1 = (int(o[2])) == 0
    # mode2 = int(o[1]) == 0
    # mode3 = int(o[0]) == 0

    mode3 = (opcode // 10000) % 10
    mode2 = (opcode // 1000) % 10
    mode1 = (opcode // 100) % 10
    instr = opcode % 100

    return (instr, mode1, mode2, mode3)

def op_to_param(program, op, mode, base):
    if mode == 0:
        return program[op]
    elif mode == 1:
        return op
    elif mode == 2:
        return program[op + base]
    else:
        print("Invalid mode")
        exit(0)

def write_op_to_param(op, mode, base):
    if mode == 0:
        return op
    elif mode == 2:
        return op + base
    else:
        print ("Invalid write mode")
        exit(0)

def run_program(program, inputs, ip):
    pc = ip
    rel_base = 0
    for i in range(10000):
        program.append(0)
    while True:
        (instr, mode1, mode2, mode3) = parse_opcode(program[pc])
        if instr == 1:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            program[write_op_to_param(op3, mode3, rel_base)] = op_to_param(program, op2, mode2, rel_base) + op_to_param(program, op1, mode1, rel_base)
            #program[op3] = (program[op2] if mode2 else op2) + (program[op1] if mode1 else op1)
            pc += 4
        elif instr == 2:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            #program[op3] = (program[op2] if mode2 else op2) * (program[op1] if mode1 else op1)
            program[write_op_to_param(op3, mode3, rel_base)] = op_to_param(program, op2, mode2, rel_base) * op_to_param(program, op1, mode1, rel_base)
            pc += 4
        elif instr == 3:
            op1 = program[pc + 1]
            #val = int(input())
            val = inputs.pop(0)
            program[write_op_to_param(op1, mode1, rel_base)] = val
            pc += 2
        elif instr == 4:
            op1 = program[pc + 1]
            pc += 2
            print(op_to_param(program, op1, mode1, rel_base))

        elif instr == 5:
            op2, op1 = (program[pc+2], program[pc+1])
            val2 = op_to_param(program, op2, mode2, rel_base)
            val1 = op_to_param(program, op1, mode1, rel_base)
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif instr == 6:
            op2, op1 = (program[pc+2], program[pc+1])
            val2 = op_to_param(program, op2, mode2, rel_base)
            val1 = op_to_param(program, op1, mode1, rel_base)
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif instr == 7:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            truth = op_to_param(program, op2, mode2, rel_base) > op_to_param(program, op1, mode1, rel_base)
            #truth = (program[op2] if mode2 else op2) > (program[op1] if mode1 else op1)
            program[write_op_to_param(op3, mode3, rel_base)] = 1 if truth else 0
            pc += 4
        elif instr == 8:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            truth = op_to_param(program, op2, mode2, rel_base) == op_to_param(program, op1, mode1, rel_base)
            program[write_op_to_param(op3, mode3, rel_base)] = 1 if truth else 0
            pc += 4
        elif instr == 9:
            op1 = program[pc+1]
            rel_base += op_to_param(program, op1, mode1, rel_base)
            pc += 2
        elif instr == 99:
            return
        else:
            print("Invalid opcode")
            #raise TypeError("um")
            return

run_program(original_program, [2], 0)