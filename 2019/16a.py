with open("16input.txt") as f:
    number = [int(x) for x in list(f.readline().rstrip())]

def pattern_for_element(pattern, element, length):
    to_return = []
    index_into_pattern = 0
    while len(to_return) <= length + 1:
        for i in range(element):
            to_return.append(pattern[index_into_pattern])
        index_into_pattern += 1
        index_into_pattern = index_into_pattern % len(pattern)
    return to_return[1:length + 1]

def generate_next_pass(number, base_pattern):
    to_return = [0]*len(number)
    for i in range(len(number)):
        pattern = pattern_for_element(base_pattern, i+1, len(number))
        accum = 0
        for j in range(len(number)):
            accum += number[j] * pattern[j]
        to_return[i] = abs(accum) % 10
    return to_return
        

pattern = [0,1,0,-1]
for i in range(100):
    number = generate_next_pass(number, pattern)
print("".join([str(x) for x in number[:8]]))

