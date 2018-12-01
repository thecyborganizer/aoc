import hashlib

input = "ojvtpuvg"
#input = "abc"
i = 0
output = [-1]*8
seeking = True
while (seeking):
	to_hash = input + str(i)
	i = i + 1
	m = hashlib.md5()
	m.update(to_hash)
	hash = m.hexdigest()
	if (i % 1000 == 0):
		print i
	if (hash[0:5] == "00000"):
		print hash
		index = int(hash[5], 16)
		if (index < 8 and output[index] == -1):
			output[index] = int(hash[6], 16)
			if ( -1 not in output):
				seeking = False
				
print output
print "".join(map(lambda x: hex(x)[2:], output))