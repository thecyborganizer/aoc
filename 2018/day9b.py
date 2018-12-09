import re
from collections import deque
text = [re.findall('\d+', s) for s in open('day9input.txt')][0]
player_count=int(text[0])
last_marble=int(text[1])

players = [0]*player_count
current_player = 3
circle = deque([0, 2, 1])
def insert(v, player):
	global circle
	global players
	if v % 23 == 0:
		players[player] += v
		#print(players[player])
		circle.rotate(8)
		players[player] += circle.pop()
		circle.rotate(-2)
		#print(players[player])
	else:
		circle.append(v)
		circle.rotate(-1)
	
for i in range(3, last_marble + 1):
	if i % 1000 == 0:
		print(i)
	insert(i, current_player)
	current_player = (current_player + 1) % player_count
	#print(circle)

print(max(players))
#print(players)