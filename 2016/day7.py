import operator
def is_quad(string):
	return (string[0] == string[3]) and (string[1] == string[2]) and not (string[0] == string[1])
	
def is_ssl(string):
	return (string[0] == string[2]) and not (string[0] == string[1])

	
def validate_ip(string):
	in_bracket = False
	has_quad = False
	has_bracket_quad = False
	has_ssl = False
	ssls = set([])
	bracket_ssls = set([])
	for i in range(len(string) - 3):
		if (string[i] == '['):
			in_bracket = True
		elif (string[i] == ']'):
			in_bracket = False
		elif (len(string) - i > 4 and is_quad(string[i:i+4])):
			if (in_bracket):
				has_bracket_quad = True
			else:
				has_quad = True
		elif (is_ssl(string[i:i+3])):
			if (in_bracket):
				bracket_ssls.add(string[i:i+3])
			else:
				ssls.add(string[i:i+3])
	for s in ssls:
		for t in bracket_ssls:
			if (s[0] == t[1]) and (s[1] == t[0]):
				has_ssl = True
	return has_ssl
		
	
				
input = []
with open("C:\Users\jkeller\Documents\AoC\day7input.txt") as f:
	input = f.readlines()


count = sum(map(validate_ip, input))
print validate_ip("xyx[xyx]xyx")
print count