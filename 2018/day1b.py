import operator, functools
frequencies = [int(line.strip()) for line in open("day1input.txt")]
sum = 0
s = set([0])
i = 0
while i < len(frequencies):
	sum += frequencies[i]
	if sum in s:
		print(sum)
		break
	s.add(sum)
	i += 1
	if i >= len(frequencies):
		i = 0
