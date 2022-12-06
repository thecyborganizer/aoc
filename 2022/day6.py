input = []
pairs = []
markerlength = 14
with open("day6input.txt") as f:
	input = f.readline().strip()[:(-1*markerlength) + 1]
	pairs = [(index+markerlength, set(list(input[index:(index+markerlength)]))) for index, x in enumerate(input)]
print(min([x[0] for x in list(filter(lambda x: len(x[1]) >= markerlength, pairs))]))