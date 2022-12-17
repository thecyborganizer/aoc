instructions = []
with open("day10input.txt") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]

def advanceCycle():
    global cycle
    global sum
    global register
    signalStrength = cycle * register
    if (cycle - 20) % 40 == 0:
        #print(signalStrength)
        sum = sum + signalStrength
    
    if register == cycle % 40 or register + 1 == cycle % 40 or register + 2 == cycle % 40:
        print("#", end="")
    else:
        print(".", end="")
    

    cycle = cycle + 1
    if (cycle-1) % 40 == 0:
        print("")


cycle = 1
register = 1
sum = 0
for i in instructions:
    if i[0] == "addx":
        advanceCycle()
        advanceCycle()
        val = int(i[1])
        register = register + val
    else:
        advanceCycle()
#print(sum)