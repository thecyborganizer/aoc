from collections import Counter
# threes = sum([sum([y[1] == 3 for y in Counter(x.strip()).most_common(10)]) for x in open("day2input.txt")])
# twos = sum(1 for line in open("day2input.txt"))
# print(threes, twos)
#print([lambda x : x == 0 for x in [0,1,2,3,4]])

def compare_boxes(a, b):
	diffs = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			diffs += 1
	return diffs

boxes = [x.strip() for x in open("day2input.txt")]

for a in boxes:
	for b in boxes:
		if compare_boxes(a,b) == 1:
			print(a)
			print(b)
#xretqmmonskvzupalfiwhcfdb