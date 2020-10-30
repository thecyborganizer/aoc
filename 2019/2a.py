program = []

with open("2input.txt") as f:
    program = [int(x) for x in f.readline().rstrip().split(",")]
#program[1] = 12
#program[2] = 2

original_program = program.copy()

def run_program():
    pc = 0

    while program[pc] != 99:
        opcode = program[pc]
        if opcode == 1:
            program[program[pc + 3]] = program[program[pc + 2]] + program[program[pc + 1]]
            pc += 4
        elif opcode == 2:
            program[program[pc + 3]] = program[program[pc + 2]] * program[program[pc + 1]]
            pc += 4

    return program[0]

for noun in range(100):
    for verb in range(100):
        print(noun, verb)
        program = original_program.copy()
        program[1] = noun
        program[2] = verb
        #print(program)
        retval = run_program()
        print(retval)
        if retval == 19690720:
            print((100 * noun) + verb)
            exit()