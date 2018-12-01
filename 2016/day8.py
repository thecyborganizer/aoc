import sys
import operator
display = [ [ 0 for i in range(50) ] for j in range(6) ]

def print_display(display):
	for row in display:
		for column in row:
			if (column == 1):
				sys.stdout.write('#')
			else:
				sys.stdout.write('.')
		sys.stdout.write('\n')

def rect(cols, rows):
	global display
	for i in range(rows):
		for j in range(cols):
			display[i][j] = 1

def rotate_row(r, val):
	global display
	row = display[r]
	new_row = [ 0 for i in range(len(row)) ]
	for i in range(len(row)):
		new_row[(i + val) % len(row)] = row[i]
	display[r] = new_row

def rotate_col(c, val):
	global display
	col = []
	new_col = [ 0 for i in range(len(display)) ]
	for row in display:
		col.append(row[c])
	for i in range(len(col)):
		new_col[(i + val) % len(col) ] = col[i]
	for i in range(len(display)):
		display[i][c] = new_col[i]
	
with open("C:\Users\jkeller\Documents\AoC\day8input.txt") as f:
	commands = map(lambda x: x.split(), f.readlines())
for command in commands:
	if (command[0] == "rect"):
		vals = command[1].split('x')
		print command, vals[0], vals[1]
		rect(int(vals[0]), int(vals[1]))
	elif (command[0] == "rotate"):
		index = int(command[2].split('=')[1])
		val = int(command[4])
		if (command[1] == "row"):
			print command, "row", index, val
			rotate_row(index, val)
		elif (command[1] == "column"):
			print command, "col", index, val
			rotate_col(index, val)
print_display(display)	
print sum(map(lambda x: sum(x), display))