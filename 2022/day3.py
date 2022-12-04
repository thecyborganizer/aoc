def thingValue(c):
	if c.isupper():
		return ord(c) - ord('A') + 27
	else:
		return ord(c) - ord('a') + 1


backpacks = []
with open("day3input.txt") as f:
	lines = [x.strip() for x in f.readlines()]
	backpacks = [[l.strip()[:len(l.strip())//2], l.strip()[len(l.strip())//2:]] for l in lines]
	groups = list(zip(lines[::3], lines[1::3], lines[2::3]))
	print(groups)

sum = 0
for line in backpacks:
	val = 0
	front = set(list(line[0]))
	for c in line[1]:
		if c in front:
			val = thingValue(c)
	sum = sum + val

gsum = 0
for g in groups:
	val = 0
	overlap = set(g[0]).intersection(set(g[1])).intersection(set(g[2]))
	gsum = gsum + thingValue(overlap.pop())

print(sum)
print(gsum)