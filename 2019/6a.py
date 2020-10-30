from anytree import Node, RenderTree, Walker

def create_children(n):
    if n.name not in d:
        return
    for c in d[n.name]:
        child = Node(c, parent=n)
        create_children(child)

def print_tree(n):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

lines = []
d = {}
#with open("6test.txt") as f:
with open("6input.txt") as f:
    lines = [tuple(x.rstrip().split(")")) for x in f.readlines()]

for l in lines:
    if l[0] in d:
        d[l[0]].append(l[1])
    else:
        d[l[0]] = [l[1]]

root = Node("COM")
create_children(root)
sum = 0
you = None
santa = None
for n in root.descendants:
    sum += n.depth
    if n.name == "YOU":
        you = n
    if n.name == "SAN":
        santa = n

print(sum)

w = Walker()
up, common, down = w.walk(you, santa)
#assuming a single common node
print(len(up) - 2 + 1 + len(down) - 1)
