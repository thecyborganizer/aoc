polymer = [x.rstrip() for x in open('day5input.txt', 'r')][0]
#polymer="dabAcCaCBAcCcaDA"
def match(a, b):
	if a.islower() and b.isupper():
		return a.upper() == b
	if a.isupper() and b.islower():
		return a == b.upper()
	return False

def get_count(text):
	reaction = False
	index = 0
	while index < len(text) - 1:
		if match(text[index], text[index+1]):
			#print("Removing ", text[index], text[index+1])
			del text[index]
			del text[index]
			index -= 1
			if index < 0:
				index = 0
			#print(len(text))
			reaction = True
		else:
			#print("no match between", text[index], text[index+1])
			index += 1
	return len(text)
	
counts = []	
for letter in range(26):
	to_remove = str(chr(97 + letter))
	test = polymer
	test = test.replace(to_remove, "")
	test = test.replace(to_remove.upper(), "")
	#print(test)
	count = get_count(list(test))
	print(count)
	counts.append(count)
print(min(counts))