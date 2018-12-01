import itertools
import copy
import os
import sys

floors = [ frozenset(["SG", "SM", "PG", "PM", "EG", "EM", "DG", "DM"]), frozenset(["TG", "RG", "RM", "CG", "CM"]), frozenset(["TM"]), frozenset([])]

generators = ["SG", "PG", "TG", "RG", "CG", "EG", "DG" ]

#floors = [ set(["HM", "LM"]), set(["HG"]), set(["LG"]), set([])]
#generators = [ "HG", "LG" ]

state = (0, floors)
root = (state, [])
def is_legal(floors):
	for floor in floors:
		for j in floor:
			if (j[1] == "M"):
				if ((j[0] + "G") not in floor):
					for i in generators:
						if i in floor:
							return False
	return True
def change_floor(floors, elev, dir):
	if elev + dir < 0:
		return []
	if elev + dir > 3:
		return []
	valid_floors = []
	for i in itertools.combinations(floors[elev], 2):
		new_floors = copy.deepcopy(floors)
		new_floors[elev] = new_floors[elev] - set(i)
		new_floors[elev+dir] = new_floors[elev+dir] | set(i)
		if is_legal(new_floors):
			valid_floors.append(new_floors)
	for i in itertools.combinations(floors[elev], 1):
		
		new_floors = copy.deepcopy(floors)
		new_floors[elev] = new_floors[elev] - set(i)
		new_floors[elev+dir] = new_floors[elev+dir] | set(i)
		if is_legal(new_floors):
			valid_floors.append(new_floors)
	return valid_floors

def is_complete(floors):
	return len(floors[3]) == (len(generators) * 2)
def to_tuple(state):
	return (state[0], state[1][0], state[1][1], state[1][2], state[1][3])
def gen_children(state):
	if (is_complete(state[1])):
		return []
	elev = state[0]
	floors = change_floor(state[1], elev, 1)
	states = zip((elev + 1 for i in range(len(floors))), floors)
	floors = change_floor(state[1], elev, -1)
	states = states + zip((elev - 1 for i in range(len(floors))), floors)
	return states
prev_states = set([])
states = gen_children(state)
next_states = []
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stdout = unbuffered
for j in range(100):
	for i in states:
		potential_next_states = gen_children(i)
		for k in potential_next_states:
			#print to_tuple(k)
			if to_tuple(k) not in prev_states:
				next_states.append(k)
				prev_states.add(to_tuple(k))
	states = next_states
	next_states = []
	for s in states:
		if is_complete(s[1]):
			print j
			print "Found solution at ", s
	print len(prev_states)