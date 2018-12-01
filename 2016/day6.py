import operator
ciphertexts=[]
with open("C:\Users\jkeller\Documents\AoC\day7input.txt") as f:
	ciphertexts = map(lambda x: x.rstrip() , f.readlines())
	
freqs = []
for i in range(8):
	freqs.append({})
print freqs
for s in ciphertexts:
	print s
	for i in range(len(list(s))):
		l = list(s)
		print i
		if (l[i] in freqs[i]):
			freqs[i][l[i]]  = freqs[i][l[i]] + 1
		else:
			freqs[i][l[i]] = 1

for d in freqs:
	#print d
	print min(d.iteritems(), key=operator.itemgetter(1))