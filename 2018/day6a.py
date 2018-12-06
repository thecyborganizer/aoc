import re
#text = [re.findall(r'\d+', x) for x in open('day6input.txt', 'r')]
text = [re.findall(r'\d+', x) for x in open('day6test.txt', 'r')]
points = list(map(lambda y: (int(y[0]), int(y[1])), text))

def distance(x1, y1, x2, y2):
	return abs(x1-x2) + abs(y1-y2)

min_x = sorted(points, key=lambda x: x[0])[0][0]
max_x = sorted(points, key=lambda x: x[0])[-1][0]
min_y = sorted(points, key=lambda x: x[1])[0][1]
max_y = sorted(points, key=lambda x: x[1])[-1][1]

print(min_x, max_x, min_y, max_y)

grid = [[0]*(max_y - min_y)]*(max_x - min_x)

for y in range(len(grid)):
	for x in range(len(grid[0])):
		xval = x + min_x
		yval = y + min_y
		index = 0
		min_distance = 9999999
		for i in range(len(points)):
			p = points[i]
			if distance(xval, yval, p[0], p[1]) < min_distance:
				#print("Distance between ", p, " and ", xval, yval, " = ", distance(xval, yval, p[0], p[1]))
				min_distance = distance(xval, yval, p[0], p[1])
				index = i
			elif distance(xval, yval, p[0], p[1]) == min_distance:
				index = -1
		#print("Setting index to ", index)
		print("updating ", yval-min_y, xval - min_x)
		grid[yval-min_y][xval-min_x] = index
	

for g in grid:
	print("".join(list(map(lambda x: chr(ord('a') + x), g))))