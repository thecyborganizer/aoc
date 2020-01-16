from collections import defaultdict

reactions = {}
quantities = {}
resources = defaultdict(int)
resources["ORE"] = 1000000000000
def fake_repr(d):
    r = ""
    for k in sorted(d.keys()):
        if k != "ORE":
            r = r + k + str(d[k])
    return r

outs = {}

with open("14input.txt") as f:
    lines = [x.rstrip().replace(">", "").split("=") for x in f.readlines()]
    for l in lines:
        key = tuple(l[1].split()[::-1])
        resource = key[0]
        quantity = int(key[1])
        value = [tuple([int(x.split()[0]), x.split()[1]]) for x in l[0].split(",")]
        reactions[resource] = value
        quantities[resource] = quantity

        outs[resource] = (quantity, value)

#print(reactions)

def consume(resource):
    global reactions
    global resources
    global quantities
    if resources[resource] > 0 or resource == "ORE":
        resources[resource] -= 1
    else:
        for t in reactions[resource]:
            item, quantity = t
            for i in range(quantity):
                #print("Consuming %s" % (item))
                consume(item)
        #make a batch, then use one
        resources[resource] += quantities[resource] - 1
        #print("Produced %d of %s, consumed %d ore" % (resources[resource], resource, -1 * resources["ORE"]))
#for i in range(460664):
#    if i % 100 == 0:
#        print(i)
#seen = set()
#seen.add(fake_repr(resources))

ore_for_one_fuel = 198984
fuel = 1000000000000 // ore_for_one_fuel
remaining_ore = 1000000000000 % ore_for_one_fuel

resources["ORE"] = remaining_ore

#while(resources["ORE"])

def make_one_fuel():
    global fuel
    consume("FUEL")
    fuel = fuel + 1

#resources["ORE"] = 198984

#make_one_fuel()

print(fuel, remaining_ore)