import re

class monkey:
    number = 0
    items = []
    operation = lambda old: old
    testDivisor = 0
    trueTarget = 0
    falseTarget = 0

    def __init__(self, number, items, operation, testDivisor, trueTarget, falseTarget):
        self.number = number
        self.items = items
        self.operation = operation
        self.testDivisor = testDivisor
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
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
for m in monkeys:
    print(m)