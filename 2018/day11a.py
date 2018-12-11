import numpy as np

serial = 7315
max_fuel = 0
max_x = -1
max_y = -1
max_size = 0
dimension = 300
width = dimension
height = dimension
grid = np.zeros((width, height), dtype=int)

for j in range(height):
	for i in range(width):
		x = i + 1
		y = j + 1
		rack_id = x + 10
		power_level = rack_id * y
		power_level += serial
		power_level *= rack_id
		hundreds = int(power_level/100) % 10
		grid[j, i] = hundreds - 5
		
#print(grid)
for k in range(1, 301):
	print(k)
	for j in range(height - (k-1)):
		for i in range(width-(k-1)):
			x = i + 1
			y = j + 1
			#print(i, j)
			sub_array = grid[j:j+k, i:i+k]
			#print(sub_array)
			#print(grid)
			total = np.sum(sub_array)
			#print(total)
			if total > max_fuel:
				max_fuel = total
				max_x = x
				max_y = y
				max_size = k

print(max_x, max_y, max_size)