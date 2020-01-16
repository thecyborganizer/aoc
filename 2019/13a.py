import itertools

class compy:

    def __init__(self, source, pc, inputs):
        # leave some room at the end
        with open(source) as f:
            self.program = [int(x) for x in f.readline().rstrip().split(",")]
        self.program += ([0] * (10000 - len(self.program)))
        self.pc = pc
        self.inputs = inputs
        self.outputs = []
        self.base = 0

    @staticmethod
    def parse_opcode(opcode):
        mode3 = (opcode // 10000) % 10
        mode2 = (opcode // 1000) % 10
        mode1 = (opcode // 100) % 10
        instr = opcode % 100

        return (instr, mode1, mode2, mode3)

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

    def run_program(self):
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
                op1 = self.program[self.pc + 1]
                val = self.inputs.pop(0)
                self.program[self.write_op_to_param(op1, mode1)] = val
                self.pc += 2
            elif instr == 4:
                op1 = self.program[self.pc + 1]
                self.outputs.append(self.op_to_param(op1, mode1))
                self.pc += 2

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

c = compy("13input.txt", 0, [2])
c.run_program()
print(c.outputs[2::3].count(2))