lines = []

with open("day1input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

(greatest, sum, sums) = (0, 0, [])
for l in lines:
    if len(l) > 0:
        sum = sum + int(l)
    else:
        if sum >= greatest:
            greatest = sum
        sums.append(sum)
        sum = 0

sums.sort()
print(greatest)
print(sums[-3] + sums[-2] + sums[-1])
