import operator

def dict_comp(a, b):
	if (a[1] < b[1]):
		return -1
	elif (a[1] > b[1]):
		return 1
	else:
		if(a[0] < b[0]):
			return 1 # opposite ordering!
		elif (a[0] > b[0]):
			return -1
		else:
			return 0

def decode(ciphertext, rotation):
	plaintext = []
	for c in list(ciphertext):
		if (c == '-'):
			plaintext.append(' ')
		else:
			int_rep = ((ord(c) - ord('a') + rotation) % 26) + ord('a')
			plaintext.append(chr(int_rep))
	return "".join(plaintext)

def generate_checksum(name):
	counts = {}
	for s in name:
		for c in list(s):
			if c in counts:
				counts[c] = counts[c] + 1
			else:
				counts[c] = 1
	sorted_counts = sorted(counts.items(), cmp=dict_comp, reverse=True)
	checksum = "".join(map(operator.itemgetter(0), sorted_counts[0:5]))
	return checksum
	
f = open('C:\Users\jkeller\Documents\AoC\day4_input.txt', 'r')
total = 0

#print decode("qzmt-zixmtkozy-ivhz",343)
for input in f:
	input_checksum = input[input.rfind("[") + 1:].rstrip().rstrip("]")
	ciphertext = input.split("-")[:-1]
	gen_checksum = generate_checksum(ciphertext)
	id = input.split("-")[-1:][0].split("[")[0]
	if (input_checksum == gen_checksum):
		print decode("-".join(ciphertext), int(id)), id
		total = total + int(id)
print total
