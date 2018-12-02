from collections import Counter
# threes = sum([sum([y[1] == 3 for y in Counter(x.strip()).most_common(10)]) for x in open("day2input.txt")])
# twos = sum(1 for line in open("day2input.txt"))
# print(threes, twos)
#print([lambda x : x == 0 for x in [0,1,2,3,4]])

counts = [Counter(x.strip()).most_common(10) for x in open("day2input.txt")]

twos = 0
threes = 0

for c in counts:
	has_two = False
	has_three = False
	for e in c:
		if e[1] == 3:
			has_three = True
		if e[1] == 2:
			has_two = True
	if has_two:
		twos+=1
	if has_three:
		threes+=1

print(twos, threes, twos*threes)