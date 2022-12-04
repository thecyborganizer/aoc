def contains(a, b):
	return a[0] <= b[0] and a[1] >= b[1]

def overlap(a, b):
	return len(set(range(a[0], a[1]  + 1)).intersection(set(range(b[0], b[1] + 1)))) > 0

with open("day4input.txt") as f:
	lines = [[[int(x) for x in l.strip().split(",")[0].split("-")], [int(y) for y in l.strip().split(",")[1].split("-")]] for l in f.readlines()]
	count = 0
	pt2count = 0
	for l in lines:
		if contains(l[0], l[1]) or contains(l[1], l[0]):
			count = count + 1
		if overlap(l[0], l[1]) or overlap(l[0], l[1]):
			pt2count = pt2count + 1
	print(count)
	print(pt2count)
