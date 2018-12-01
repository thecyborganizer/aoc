input = open('C:\Users\jkeller\Documents\AoC\day3_input.txt', 'r')

impossible = 0
possible = 0
triangles = []
lines = []
def get_max(triangle):
	max = 0
	max_index = 0
	for i in range(len(triangle)):
		if int(triangle[i]) > int(max):
			max = triangle[i]
			max_index = i
	return max_index

def is_possible(triangle):
	max_index = get_max(triangle)
	smaller_legs = 0
	for i in range(len(triangle)):
		if (i != max_index):
			smaller_legs = smaller_legs + triangle[i]
	if (smaller_legs <= triangle[max_index]):
		return False
	else:
		return True

def read_three_lines(input):
	triangles = [[],[],[]]
	for i in range(3):
		for j in range(3):
			triangles[j].append(input[i][j])
	return triangles

for line in input:
	lines.append(map(int, line.split()))

for i in range(0, len(lines), 3):
	triangles = triangles + read_three_lines(lines)
	del lines[0:3]

for triangle in triangles:
	if (is_possible(triangle)):
		possible = possible + 1
	else:
		impossible = impossible + 1
print possible, impossible