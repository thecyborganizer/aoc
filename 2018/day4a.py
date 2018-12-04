from datetime import datetime
import re
logs = [x.rstrip() for x in open('day4input.txt', 'r')]

def parse_event(e):
	if e == 'wakes up':
		return 1
	elif e == 'falls asleep':
		return 0
	else:
		return int(re.search(r'\d+', e).group())

events = sorted([(datetime.strptime(re.search(r'\[.+\]', x).group().strip('[]'), '%Y-%m-%d %H:%M'), parse_event(' '.join(x.split()[2:]))) for x in logs], key=lambda y: y[0])

for e in events:
	print(e[0], e[1])
	
guard_sleeps = {}

id = 0
last_event_time = 0
for e in events:
	if e[1] > 1:
		id = e[1]
	if e[1] == 1:
		for i in range(last_event_time.minute, e[0].minute):
			if id in guard_sleeps:
				guard_sleeps[id][i] += 1
			else:
				guard_sleeps[id] = [0]*60
				guard_sleeps[id][i] += 1
		
	last_event_time = e[0]

max_value = 0
max_id = 0
for k in guard_sleeps.keys():
	if sum(guard_sleeps[k]) > max_value:
		max_id = k
		max_value = sum(guard_sleeps[k])

print(max_id, guard_sleeps[max_id].index(max(guard_sleeps[max_id])))