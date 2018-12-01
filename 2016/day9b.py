import re
def count(string):
	m = re.search(r'\((\d+)x(\d+)\)',string)
	c = 0
	if not m:
		return len(string)
	i = string.find(')') + 1
	length = int(m.groups()[0])
	repeats = int(m.groups()[1])
	repeat_string = string[i:i + length]
	c = c + repeats * count(repeat_string)
	k = string.find('(')
	return k + c + count(string[i + length:])
	
with open("C:\Users\jkeller\Documents\AoC\day9input.txt") as f:
	input = f.readline().rstrip()
	print count(input)