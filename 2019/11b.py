import itertools

original_program = []

loc = (0,0)
facing = 0 #N, E, S, W
whites = set()
output_queue = []

#with open("11test.txt") as f:
with open("11input.txt") as f:
    original_program = [int(x) for x in f.readline().rstrip().split(",")]

def parse_opcode(opcode):
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

def consume_input(inputs):
    global loc
    global whites
    if loc in whites:
        return 1
    else:
        return 0

def advance(l, f):
    if f == 0:
        return (l[0], l[1] + 1)
    elif f == 1:
        return (l[0] + 1, l[1])
    elif f == 2:
        return (l[0], l[1] - 1)
    elif f == 3:
        return (l[0] - 1, l[1])
    else:
        print("Invalid facingection")
        exit(0)
        return

def produce_output(o):
    global loc
    global whites
    global output_queue
    global facing
    output_queue.append(o)
    if len(output_queue) == 2:
        color = output_queue.pop(0)
        if color == 1:
            whites.add(loc)
        elif color == 0:
            if loc in whites:
                whites.remove(loc)
        else:
            print("Invalid color")
            exit(0)
        turn = output_queue.pop(0)
        if turn == 1:
            facing = (facing + 1) % 4
        elif turn == 0: 
            facing = (facing - 1) % 4
        else:
            print("Invalid turn instruction")
            exit(0)
        loc = advance(loc, facing)
        


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
            pc += 4
        elif instr == 2:
            op3, op2, op1 = (program[pc+3], program[pc+2], program[pc+1])
            program[write_op_to_param(op3, mode3, rel_base)] = op_to_param(program, op2, mode2, rel_base) * op_to_param(program, op1, mode1, rel_base)
            pc += 4
        elif instr == 3:
            op1 = program[pc + 1]
            #val = inputs.pop(0)
            val = consume_input(inputs)
            program[write_op_to_param(op1, mode1, rel_base)] = val
            pc += 2
        elif instr == 4:
            op1 = program[pc + 1]
            #print(op_to_param(program, op1, mode1, rel_base))
            produce_output(op_to_param(program, op1, mode1, rel_base))
            pc += 2

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
            return

whites.add((0,0))
print(whites)
run_program(original_program, [], 0)



for i in range(-40, 40):
    for j in range(-40, 40):
        if (i,j) in whites:
            print("#", end="")
        else:
            print(" ", end="")
    print()
