text = [x.rstrip() for x in open('day12input.txt', 'r')]
#text = [x.rstrip() for x in open('day12test.txt', 'r')]

def print_state(state):
    for s in state:
        if s:
            print('#', end='')
        else:
            print('.', end='')
    print("")



state = list(map(lambda x : x == '#', list(text[0])))
for i in range(3):
    state.insert(0, False)
    state.append(False)
rules_txt = [(list(map(lambda x: x == '#', x.split('=>')[0].strip())), list(map(lambda x: x == '#', x.split('=>')[1].strip()))) for x in text[2:]]
rules = set()
for r in rules_txt:
    if r[1][0]:
        rules.add(tuple(r[0]))
offset = -3
print(0, offset)
print_state(state)
for i in range(1, 5001):
    if i % 100 == 0:
        print(i)
        print(len(state))
    low_count = 0
    high_count = 0
    next_gen = [False, False]
    for j in range(2, len(state)-2):
        local_state = tuple(state[j-2:j+3])
        if local_state in rules:
            next_gen.append(True)
            if j == 2:
                low_count += 1
            if j == len(state) - 3:
                high_count += 1
        else:
            next_gen.append(False)
    next_gen.append(False)
    next_gen.append(False)
    if low_count > 0:
        next_gen.insert(0, False)
        offset -= 1
    if high_count > 0:
        next_gen.append(False)
    if next_gen[3] == False:
        del next_gen[0]
        offset += 1
    state = next_gen
    #print(i, offset)
print(offset)
print_state(state)
offset = 50000000000 - 81
score = 0
for i in range(len(state)):
    if state[i]:
        score += i + offset

print(score)