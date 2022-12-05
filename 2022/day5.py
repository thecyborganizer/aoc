import re

global stacks
def move(quantity, src, dest):
	for _ in range(quantity):
		stacks[dest].append(stacks[src].pop())

def move2(quantity, src, dest):
	tmp = []
	for _ in range(quantity):
		tmp.append(stacks[src].pop())
	tmp.reverse()
	stacks[dest].extend(tmp)

stacklines = []
instrlines = []
with open("day5input.txt") as f:
	lines = [x[:-1] for x in f.readlines()]
	stacklines = [x[1::4] for x in lines[0:8]]
	#stacklines = [x[1::4] for x in lines[0:3]]

	stacklines.reverse()
	instrlines = lines[10:]
	#instrlines = lines[5:]

stacks = [[] for _ in range(len(stacklines[0]))]
for line in stacklines:
	for i in range(len(line)):
		if line[i] != " ":
			stacks[i].append(line[i])
print(stacks)
for instr in instrlines:
	vals = [int(x) for x in re.findall('\d+', instr)]
	move2(vals[0], vals[1] - 1, vals[2] - 1)
	print(stacks)

print("".join([stack[-1] for stack in stacks]))