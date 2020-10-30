with open("16input.txt") as f:
    number_txt = f.readline().rstrip()
    offset = int(number_txt[:7])
    number = [int(x) for _ in range(10000) for x in number_txt][offset:]

for i in range(100):
    print(i)
    for j in range(-2, -(len(number) + 1),-1):
        number[j] = (number[j] + number[j+1]) % 10

print("".join([str(x) for x in number[:8]]))