import itertools
import sys
import operator
import random

class compy:

    def __init__(self, source, pc, inputs, input_func, output_func):
        # leave some room at the end
        if source != "":
            with open(source) as f:
                self.program = [int(x) for x in f.readline().rstrip().split(",")]
            self.program += ([0] * (10000 - len(self.program)))
        else:
            self.program = [0] * 10000
        self.pc = pc
        self.inputs = inputs
        self.outputs = []
        self.base = 0
        self.input_func = input_func
        self.output_func = output_func

    @staticmethod
    def parse_opcode(opcode):
        mode3 = (opcode // 10000) % 10
        mode2 = (opcode // 1000) % 10
        mode1 = (opcode // 100) % 10
        instr = opcode % 100

        return (instr, mode1, mode2, mode3)

    def clone(self):
        return compy(self)

    def op_to_param(self, op, mode):
        if mode == 0:
            return self.program[op]
        elif mode == 1:
            return op
        elif mode == 2:
            return self.program[op + self.base]
        else:
            print("Invalid mode")
            exit(0)
    
    def write_op_to_param(self, op, mode):
        if mode == 0:
            return op
        elif mode == 2:
            return op + self.base
        else:
            print ("Invalid write mode")
            exit(0)

    def produce_output(self):
        while True:
            (instr, mode1, mode2, mode3) = compy.parse_opcode(self.program[self.pc])
            if instr == 1:
                op3, op2, op1 = (self.program[self.pc+3], self.program[self.pc+2], self.program[self.pc+1])
                self.program[self.write_op_to_param(op3, mode3)] = self.op_to_param(op2, mode2) +self.op_to_param(op1, mode1)
                self.pc += 4
            elif instr == 2:
                op3, op2, op1 = (self.program[self.pc+3], self.program[self.pc+2], self.program[self.pc+1])
                self.program[self.write_op_to_param(op3, mode3)] = self.op_to_param(op2, mode2) * self.op_to_param(op1, mode1)
                self.pc += 4
            elif instr == 3:
                self.input_func(self.inputs)
                op1 = self.program[self.pc + 1]
                val = self.inputs.pop(0)
                self.program[self.write_op_to_param(op1, mode1)] = val
                self.pc += 2
            elif instr == 4:
                op1 = self.program[self.pc + 1]
                self.outputs.append(self.op_to_param(op1, mode1))
                #self.output_func(self.outputs)
                self.pc += 2
                return self.outputs.pop(0)
                
            elif instr == 5:
                op2, op1 = (self.program[self.pc+2], self.program[self.pc+1])
                val2 = self.op_to_param(op2, mode2)
                val1 = self.op_to_param(op1, mode1)
                if val1 != 0:
                    self.pc = val2
                else:
                    self.pc += 3
            elif instr == 6:
                op2, op1 = (self.program[self.pc+2], self.program[self.pc+1])
                val2 =self.op_to_param(op2, mode2)
                val1 =self.op_to_param(op1, mode1)
                if val1 == 0:
                    self.pc = val2
                else:
                    self.pc += 3
            elif instr == 7:
                op3, op2, op1 = (self.program[self.pc+3], self.program[self.pc+2], self.program[self.pc+1])
                truth =self.op_to_param(op2, mode2) > self.op_to_param(op1, mode1)
                self.program[self.write_op_to_param(op3, mode3)] = 1 if truth else 0
                self.pc += 4
            elif instr == 8:
                op3, op2, op1 = (self.program[self.pc+3], self.program[self.pc+2], self.program[self.pc+1])
                truth =self.op_to_param(op2, mode2) == self.op_to_param(op1, mode1)
                self.program[self.write_op_to_param(op3, mode3)] = 1 if truth else 0
                self.pc += 4
            elif instr == 9:
                op1 = self.program[self.pc+1]
                self.base +=self.op_to_param(op1, mode1)
                self.pc += 2
            elif instr == 99:
                return
            else:
                print("Invalid opcode")
                return

class explorer:
    def __init__(self, comp, x, y):
        self.comp = comp
        self.x = x
        self.y = y

    def move(self, direction):
        global walls, space, moves, solution
        self.comp.inputs = [direction]
        retval = self.comp.produce_output()
        new_x = moves[direction-1][0] + self.x
        new_y = moves[direction-1][1] + self.y
        if retval == 2:
            solution.add((new_x, new_y))
            self.x, self.y = new_x, new_y
        elif retval == 0:
            walls.add((new_x, new_y))
        else:
            space.add((new_x, new_y))
            self.x, self.y = new_x, new_y
        return retval

walls = set()
space = set()
solution = set()
space.add((0, 0))

def clone(c):
    new_compy = compy("", c.pc, [], c.input_func, c.output_func)
    new_compy.program = c.program[:]
    new_compy.pc = c.pc
    new_compy.inputs = c.inputs[:]
    new_compy.outputs = c.outputs[:]
    new_compy.base = c.base
    new_compy.input_func = c.input_func
    new_compy.output_func = c.output_func
    return new_compy


def input_func(inputs):
    return

def output_func(outputs):
    response = outputs.pop(0)
    yield response

def turn_right(direction):
    if direction == 1:
        return 3
    elif direction == 2: 
        return 4
    elif direction == 3:
        return 2
    elif direction == 4:
        return 1

#moves = [(1, 0), (-1, 0), (0, 1), (0, -1)] # N, S, E, W
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

e = explorer(compy("15input.txt", 0, [1], input_func, output_func), 0, 0)
direction = 1
retval = -1
#while retval != 2:
for i in range(1000000):
    retval = e.move(direction)
    #if retval == 0:
    #direction = turn_right(direction)
    direction = random.randint(1,4)
    #print(e.x, e.y)
    #print (walls)
    #print (space)

min_x = min([a[0] for a in walls] + [a[0] for a in space])
min_y = min([a[1] for a in walls] + [a[1] for a in space])
max_x = max([a[0] for a in walls] + [a[0] for a in space])
max_y = max([a[1] for a in walls] + [a[1] for a in space])

x_offset = abs(min(min_x, 0))
x_dim = (max_x - min_x) + 1
y_offset = abs(min(min_y, 0))
y_dim = (max_y - min_y) + 1

grid = [["" for i in range(x_dim)] for j in range(y_dim)]
#print (x_offset, y_offset)
#print (x_dim, y_dim)
#print (e.x, e.y)
with open("maze.txt", "a") as f:
    f.write(str(walls))
    f.write(str(space))
    f.write(str(solution))
#print (walls)
#print (space)
#print (solution)

for j in range(len(grid)):
    for i in range(len(grid[0])):
        x, y = i - x_offset, j - y_offset
        char = " "
        if (x, y) == (0, 0):
            char = "X"
        elif (x, y) in space:
            char = "."
        elif (x, y) in walls:
            char = "#"
        elif (x, y) in solution:
            char = "!"
        grid[j][i] = char    

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end="")
    print(" ")



#queue = [compy("15input.txt", 0, [1], input_func, output_func)]

# for i in range(1,5):
#     queue.append(compy("15input.txt", 0, [i], input_func, output_func))

# while len(queue) != 0:
#     if len(queue) % 1000 == 0:
#         print(len(queue))
#     current_state = queue.pop(0)
#     retval = next(current_state.run_program())
#     if retval == 2:
#         print("found it")
#     elif retval == 1:
#         for i in range(1,5):
#             new_compy = clone(current_state)
#             new_compy.inputs = [i]
#             queue.append(new_compy)