valids = 0

def adjacent_digits(digits):
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1] and digits.count(digits[i]) == 2:
            return True
    return False

def never_decrease(digits):
    for i in range(len(digits) - 1):
        if digits[i+1] < digits[i]:
            return False
    return True

#for i in range(111111, 111112):
for i in range(264793,803935+1):
    condition = False
    digits = [int(x) for x in list(str(i))]
    if adjacent_digits(digits) and never_decrease(digits):
        valids += 1

print(valids)
