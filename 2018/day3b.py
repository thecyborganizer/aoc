class claim:
	def __init__(self, id, x, y, w, h):
		self.id=id
		self.x=x
		self.y=y
		self.w=w
		self.h=h
	def __repr__(self):
		return ",".join([str(self.id), str(self.x), str(self.y), str(self.w), str(self.h)]) 
	def count_claim(self, dict):
		for i in range(self.x, self.x + self.w):
			for j in range(self.y, self.y + self.h):
				if (i, j) in dict:
					dict[(i,j)] += 1
				else:
					dict[(i,j)] = 1
					
t = [x.split() for x in open('day3input.txt', 'r')]
claims = []
counts = {}
for c in t:
	id = int(c[0][1:])
	x = int(c[2].split(',')[0])
	y = int(c[2].split(',')[1][:-1])
	w = int(c[3].split('x')[0])
	h = int(c[3].split('x')[1])
	new_claim = claim(id, x, y, w, h)
	claims.append(new_claim)

for claim in claims:
	claim.count_claim(counts)

for claim in claims:
	is_unique = True
	for i in range(claim.x, claim.x + claim.w):
		for j in range(claim.y, claim.y + claim.h):
			if counts[(i, j)] > 1:
				is_unique = False
	if is_unique:
		print(claim.id)
