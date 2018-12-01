from sets import Set

keypad = [[0xE, 0xE, 0x1, 0xE, 0xE], [0xE, 0x2, 0x3, 0x4, 0xE], [0x5, 0x6, 0x7, 0x8, 0x9], [0xE, 0xA, 0xB, 0xC, 0xE], [0xE, 0xE, 0xD, 0xE, 0xE]]

def validate_move(x, y):
	if (x < 0 or x > 4 or y < 0 or y > 4):
		return False
	if (keypad[y][x] == 0xE):
		return False
	return True

def go_north(x,y):
	if (validate_move(x,y-1)):
		return (x,y-1)
	return (x, y)
def go_east(x,y):
	if (validate_move(x+1, y)):
		return (x+1,y)
	return (x, y)
def go_south(x,y):
	if (validate_move(x, y+1)):
		return (x,y+1)
	return (x, y)
def go_west(x,y):
	if (validate_move(x-1, y)):
		return (x-1,y)
	return (x, y)

def move(x, y, c):
	if (c == "U"):
		return go_north(x,y)
	elif (c == "R"):
		return go_east(x,y)
	elif (c == "D"):
		return go_south(x,y)
	elif (c == "L"):
		return go_west(x,y)
	else:
		print "Invalid input character: " + c
		return (0,0)
input = open('C:\Users\jkeller\Documents\AoC\day2_input.txt', 'r')

x = 0
y = 2

for line in input:
	l = list(line.rstrip())
	for i in l:
		(x,y) = move(x,y,i)
	print hex(keypad[y][x])
		
	