import collections

with open("14input.txt") as f:

    outs = {}

    lines = [x.rstrip().replace(">", "").split("=") for x in f.readlines()]
    for l in lines:
        key = tuple(l[1].split()[::-1])
        resource = key[0]
        quantity = int(key[1])
        value = [tuple([int(x.split()[0]), x.split()[1]]) for x in l[0].split(",")]
        #reactions[resource] = value
        #quantities[resource] = quantity

        outs[resource] = (quantity, value)

    def make_fuel(fuel):
        print("Making %d fuel" % fuel)
        need = {"FUEL": fuel}
        have = collections.defaultdict(int)
        while True:
            try:
                next_needed = next(n for n in need if n != "ORE")
            except StopIteration:
                break
            quantity_to_make, inputs = outs[next_needed]
            # How many batches do we need to do? How much will be left over?
            batches, leftover = divmod(need[next_needed], quantity_to_make)
            del need[next_needed]
            if leftover != 0:
                batches += 1
                have[next_needed] = quantity_to_make - leftover
            for quantity, ingredient in inputs:
                need[ingredient] = need.get(ingredient, 0) + batches * quantity - have[ingredient]
                del have[ingredient]
        return need['ORE']


lower = 1
upper = 2

while make_fuel(upper) < 10**12:
    lower = upper
    upper = upper * 2

while upper != lower + 1:
    ore = make_fuel((lower + upper) // 2)
    if ore < 10**12:
        lower = (lower + upper) // 2
    else:
        upper = (lower + upper) // 2

print(lower)
print(make_fuel(7659732))