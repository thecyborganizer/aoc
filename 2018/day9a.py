import re
text = [re.findall('\d+', s) for s in open('day9input.txt')][0]
player_count=int(text[0])
last_marble=int(text[1])

players = [0]*player_count
current_player = 3
circle = [0, 2, 1]
cmi = 1
def insert(c, v, cmi, player, players):
	if v % 23 == 0:
		players[player] += v
		to_remove = cmi - 7
		if to_remove < 0:
			to_remove += len(c)
		players[player] += c[to_remove]
		del c[to_remove]
		if to_remove == len(c):
			cmi = 0
		else:
			cmi = to_remove
		return c, cmi
	to_insert = cmi + 2
	if to_insert == len(c):
		c.append(v)
		cmi = to_insert
		return c, cmi
	elif to_insert == len(c) + 1:
		to_insert = 1
	c.insert(to_insert, v)
	cmi = to_insert
	return c, cmi

for i in range(3, last_marble + 1):
	if i % 1000 == 0:
		print(i)
	circle, cmi = insert(circle, i, cmi, current_player, players)
	current_player = (current_player + 1) % player_count
	# for k in range(len(circle)):
		# if k == cmi:
			# print("(", circle[k], "),", end='')
		# else:
			# print(circle[k], ",", end='')
	# print("")

print(max(players))