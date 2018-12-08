import sys
from collections import deque

text = list(map(lambda x: int(x), [x.strip() for x in open('day8input.txt', 'r')][0].split()))
#text = [x.strip() for x in open('day8test.txt', 'r')][0].split()
total = 0

depth = 0
i=0
d = deque()
while i < len(text)-1:
	num_children = text[i]
	metadata_count = text[i+1]
	i += 2
	deque.push((num_children, metadata_count, depth))
	if num_children == 0:
		(n, m, d) = deque.pop()
		total += sum(text[i:i+m])
		i += m
		depth -= 1
		while deque[-1]
	else:
		depth += 1
		
	