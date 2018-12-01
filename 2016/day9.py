
def decompress(string):
	expansion = False
	i = 0
	output = ""
	while (i < len(string)):
		if expansion:
			j = string.find(')', i)
			expansion_string = string[i:j].split('x')
			length = int(expansion_string[0])
			repeats = int(expansion_string[1])
			#print expansion_string
			i = j + 1
			repeated_string = string[i:i+length]
			i = i + length
			#print length, repeats, repeated_string, i
			for k in range(repeats):
				output = output + repeated_string
			expansion = False
		else:
			if string[i] == '(':
				expansion = True
			else:
				output = output + string[i]
				#print i, string, output
			i = i + 1
	return output
	
with open("C:\Users\jkeller\Documents\AoC\day9input.txt") as f:
	input = f.readline().rstrip()
	print len(decompress(input))