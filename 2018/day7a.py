from operator import itemgetter
#class node(i, d):
#	self.id = i
#	self.children = d
	
reqs = {}
letters = set()
text = [itemgetter(1,7)(x.split()) for x in open('day7input.txt', 'r')]
#text = [itemgetter(1,7)(x.split()) for x in open('day7test.txt', 'r')]
queue = []
for t in text:
	if t[1] in reqs:
		reqs[t[1]].append(t[0])
	else:
		reqs[t[1]] = [t[0]]
	letters.add(t[1])
	letters.add(t[0])
queue_len = 5
time_to_finish = 60
num_chars = 26
for l in sorted(list(letters)):
	if l in reqs:
		reqs[l].sort()
		print(l, reqs[l])
	else:
		print(l, "[]")
to_remove = []
time = -1
while len(to_remove) < num_chars:	
	time += 1
	i = 0
	print(queue)
	while i < len(queue):
		queue[i] = (queue[i][0], queue[i][1] - 1)
		if(queue[i][1] == 0):
			to_remove.append(queue[i][0])
			for k in list(reqs):
				if queue[i][0] in reqs[k]:
					reqs[k].remove(queue[i][0])
				if len(reqs[k]) == 0:
					reqs.pop(k)
			del queue[i]
		else:
			i += 1
	for l in sorted(list(letters)):
		if l not in reqs and len(queue) < queue_len:
			letters.remove(l)
			queue.append((l, time_to_finish + ord(l) - ord('A') + 1))

print ("".join(to_remove))
print(time)