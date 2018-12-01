from sets import Set

input = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5".split(", ")

#input = "R5, L5, R5, R3".split(", ")

#input = "R8, R4, R4, R8".split(", ")

print input

orientation = 0
x = 0
y = 0

visits = Set([])

def rotate(direction):
	if (direction == "R"):
		return (orientation + 1) % 4
	elif (direction == "L"):
		return (orientation - 1) % 4
	else:
		print "Invalid input for rotation"
		return 0

def update_visits(v, type, startx, starty, count):
	if (type == "x"):
		for i in range(count):
			if (startx + i, starty) in v:
				print "Re-visiting " + str(startx + i) + "," + str(starty)
				if (len(v) < 50):
					print v
			else:
				v.add((startx + i, starty))
	elif (type == "y"):
		for i in range(count):
			if (startx, starty+i) in v:
				print "Re-visiting " + str(startx) + "," + str(starty+i)
				if (len(v) <50):
					print v
			else:
				v.add((startx, starty+i))
	else:
		print "what have you done"

def try_insert(x,y,v):
	if (x,y) in v:
		print "Repeat visit at " + str(x) + "," + str(y) + ", distance is " + str(abs(x) + abs(y))
	else:
		v.add((x,y))
		
def go_north(x,y,v):
	try_insert(x, y+1, v)
	return (x, y+1)
def go_east(x,y,v):
	try_insert(x+1, y, v)
	return (x+1, y)
def go_south(x,y,v):
	try_insert(x, y-1, v)
	return (x, y-1)
def go_west(x,y,v):
	try_insert(x-1, y, v)
	return (x-1, y)
		
def distance(o, l, x, y, v):
	if (o == 0):
		for i in range(l):
			(x,y) = go_north(x,y,v)
			#print "Went to " + str(x) + "," +str(y)
		return (x,y)
	elif (o == 1):
		for i in range(l):
			(x,y) = go_east(x,y,v)
			#print "Went to " + str(x) + "," +str(y)
		return (x,y)
	elif (o == 2):
		for i in range(l):
			(x,y) = go_south(x,y,v)
			#print "Went to " + str(x) + "," +str(y)
		return (x,y)
	elif (o == 3):
		for i in range(l):
			(x,y) = go_west(x,y,v)
			#print "Went to " + str(x) + "," +str(y)
		return (x,y)
	else:
		print "Invalid input for distance"
		return (0,0)

for i in input:
	orientation = rotate(i[0])
	(x,y) = distance(orientation, int(i[1:]), x, y, visits)
	
print abs(x) + abs(y)