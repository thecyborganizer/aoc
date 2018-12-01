class bot(object):
	def __init__(self, i):
		self.num = i
		self.chips = []
		self.targets = []
bots = [ bot(i) for i in range(300)]
outputs = [ [] for i in range(300)]

def assign_value(bots, bot, val):
	bot.chips.append(val)
	bot.chips.sort()
	return attempt_give_away(bots, bot, [])


def attempt_give_away(bots, bot, instructions):
	if (len(instructions) == 2):
		bot.targets = bot.targets + instructions
	if (len(bot.chips) == 2 and len(bot.targets) == 2):
		return give_away(bots, bot, bot.targets[0], bot.targets[1])
	else:
		return bots

def give_away(bots, bot, lo_t, hi_t):
	global outputs
	if (bot.chips[0] == 17 and bot.chips[1] == 61):
		print "bot ", bot.num, " is comparing 17 and 61"
	if(lo_t[0] == 'output'):
		outputs[lo_t[1]].append(bot.chips[0])
		del bot.chips[0]
	else:
		bots = assign_value(bots, bots[lo_t[1]], bot.chips[0])
		del bot.chips[0]
	if(hi_t[0] == 'output'):
		outputs[hi_t[1]].append(bot.chips[-1])
		del bot.chips[-1]
	else:
		#print bot.num, lo_t, hi_t, bot.chips
		bots = assign_value(bots, bots[hi_t[1]], bot.chips[-1])
		del bot.chips[-1]
	
	return bots
input = []
with open("C:\Users\jkeller\Documents\AoC\day10input.txt") as f:
	input = map(lambda x : x.split(), f.readlines())
	
for cmd in input:
	print cmd
	if (cmd[0] == 'value'):
		assign_value(bots, bots[int(cmd[5])], int(cmd[1]))
	else:
		instructions = [ [cmd[5], int(cmd[6])], [cmd[10], int(cmd[11])] ]
		attempt_give_away(bots, bots[int(cmd[1])], instructions)
		
print outputs