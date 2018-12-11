import re
text = [re.findall(r'-?\d+', x) for x in open('day10input.txt', 'r')]
#text = [re.findall(r'-?\d+', x) for x in open('day10test.txt', 'r')]
state = [(int(x[0]), int(x[1]), int(x[2]), int(x[3])) for x in text]
max_x = max([s[0] for s in state])
min_x = min([s[0] for s in state])
max_y = max([s[1] for s in state])
min_y = min([s[1] for s in state])
t = 0
found = False
while found == False:
	t += 1
	if t % 1000 == 0:
		print(t)
	xes = {}
	ys = {}
	for i in range(len(state)):
		state[i] = (state[i][0] + state[i][2], state[i][1] + state[i][3], state[i][2], state[i][3])
		if state[i][0] in xes:
			xes[state[i][0]] += 1
		else:
			xes[state[i][0]] = 1
		if state[i][1] in ys:
			ys[state[i][1]] += 1
		else:
			ys[state[i][1]] = 1
	loc_set = set([(s[0], s[1]) for s in state])
	for l in loc_set:
		for i in range(1,8):
			if (l[0], l[1] + i) not in loc_set:
				break
			if i == 7:
				found = True
	#if max(xes.values()) >= 8 and max(ys.values()) >= 6:
	#	found = True
	
print("got here")
max_x = max([s[0] for s in state])
min_x = min([s[0] for s in state])
max_y = max([s[1] for s in state])
min_y = min([s[1] for s in state])
lset = set([(s[0], s[1]) for s in state])
print(max_x, min_x, max_y, min_y)
print(len(state))
for j in range(min_y, max_y+1):
	for i in range(min_x, int((max_x+1))):
		if (i, j) in lset:
			print('#', end='')
		else:
			print('.', end='')
	print("")
print(t)