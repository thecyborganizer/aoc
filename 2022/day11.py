import re
from operator import mul
from functools import reduce

class monkey:
    number = 0
    items = []
    operation = lambda old: old
    testDivisor = 0
    trueTarget = 0
    falseTarget = 0
    inspectionCount = 0
    type = ""
    itemsAsModuluses = []

    def __init__(self, number, items, operation, testDivisor, trueTarget, falseTarget):
        self.number = number
        self.items = items
        self.operation = operation
        self.testDivisor = testDivisor
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.itemsAsModuluses = []
    def __str__(self):
        return "Monkey {}:\n  Starting items: {}\n    Operation: {}\n    Test: {}\nTrue:{}\nFalse:{}\n".format(self.number, self.items, self.operation, self.testDivisor, self.trueTarget, self.falseTarget)
    def parseMonkey(monkeyText):
        number = [int(x) for x in re.findall('\d+', monkeyText[0])][0]
        items = [int(x) for x in re.findall('\d+', monkeyText[1])]
        operation = lambda old: old
        opText = monkeyText[2].split(" = ")[1]
        opNumbers = [int(x) for x in re.findall('\d+', monkeyText[2])]
        if opText.find("+") > 0:
            operation = lambda old: old + int(opText.split(" + ")[1])
        elif opText.find("*") > 0 and len(opNumbers) > 0:
            operation = lambda old: old * opNumbers[0]
        else:
            operation = lambda old: old * old
        testDivisor = [int(x) for x in re.findall('\d+', monkeyText[3])][0]
        trueTarget = [int(x) for x in re.findall('\d+', monkeyText[4])][0]
        falseTarget = [int(x) for x in re.findall('\d+', monkeyText[5])][0]
        return monkey(number, items, operation, testDivisor, trueTarget, falseTarget)

monkeys = []
with open("day11input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    for i in range(0, len(lines), 7):
        monkeys.append(monkey.parseMonkey(lines[i:i+6]))
# for r in range(600):
#     for m in monkeys:
#         while len(m.items) > 0:
#             m.inspectionCount = m.inspectionCount + 1
#             item = m.items.pop(0)
#             item = m.operation(item)
#             if item % m.testDivisor == 0:
#                 monkeys[m.trueTarget].items.append(item)
#             else:
#                 monkeys[m.falseTarget].items.append(item)

# monkeys.sort(key=lambda m: m.inspectionCount, reverse=True)
# print([m.inspectionCount for m in monkeys])
# print(reduce(mul, [m.inspectionCount for m in monkeys[0:2]], 1))

divisors = [m.testDivisor for m in monkeys]

for m in monkeys:
    for i in m.items:
        dictionary = {}
        for d in divisors:
            dictionary[d] = i % d
        m.itemsAsModuluses.append(dictionary)

for r in range(10000):
    for m in monkeys:
        while len(m.itemsAsModuluses) > 0:
            m.inspectionCount = m.inspectionCount + 1
            item = m.itemsAsModuluses.pop(0)
            for d in divisors:
                item[d] = m.operation(item[d]) % d
            if item[m.testDivisor] == 0:
                monkeys[m.trueTarget].itemsAsModuluses.append(item)
            else:
                monkeys[m.falseTarget].itemsAsModuluses.append(item)

monkeys.sort(key=lambda m: m.inspectionCount, reverse=True)
print(reduce(mul, [m.inspectionCount for m in monkeys[0:2]], 1))
