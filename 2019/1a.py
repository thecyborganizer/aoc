l = []

def calc_fuel(n):
    k = int(float(n)/3) - 2
    if k <= 0:
        return 0
    else:
        return k + calc_fuel(k)

print(calc_fuel(100756))

with open("1input.txt") as f:
    l = [calc_fuel(int(x.rstrip())) for x in f.readlines()]
print(sum(l))