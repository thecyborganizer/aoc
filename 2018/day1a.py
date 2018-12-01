import operator, functools
frequencies = [int(line.strip()) for line in open("day1input.txt")]
print(functools.reduce(lambda x, y: x+y, frequencies))