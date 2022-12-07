import sys
class node:
    name = ""
    children = []
    size = 0
    parent = ""
    type = ""
    def __init__(self, name, size=0, parent="", type="file"):
        self.name=name
        self.size=size
        self.parent=parent
        self.children = []
        self.type=type
    def __str__(self):
        return "{} {} {}".format(self.name, self.size, [n.name for n in self.children])

def printTree(node, depth):
    if node.size != 0:
        print("{} - {} ({}, size={}".format("  "*depth, node.name, node.type, node.size))
        return
    print("{} - {} ({}, size={})".format("  "*depth, node.name, node.type, node.size))
    for n in node.children:
        printTree(n, depth+1)


def nodeSize(node):
    if node.type == "file":
        return node.size
    else:
        sum = 0
        for n in node.children:
            sum = sum + nodeSize(n)
        node.size = sum
        return sum

smallNodes = 0

def findSmallNodes(node):
    global smallNodes
    if node.type == "dir":
        if node.size < 100000:
            smallNodes = smallNodes + node.size
        for n in node.children:
            findSmallNodes(n)

directoryToDelete = ""
minSizeSoFar = sys.maxsize

def findDirectoryToDelete(node, spaceNeeded):
    global minSizeSoFar
    if node.type == "dir":
        if node.size > spaceNeeded and node.size < minSizeSoFar:
            minSizeSoFar = node.size
        for n in node.children:
            findDirectoryToDelete(n, spaceNeeded)

root = node("/", 0, "", "dir")
currentNode = root
with open("day7input.txt") as f:
    lines = [x.strip() for x in f.readlines()[1:]]
    index = 0
    while index < len(lines):
        line = lines[index]
        if line[0] == "$":
            if line[2:4] == "cd":
                name = line[5:]
                if name == "..":
                   currentNode = currentNode.parent
                else:
                   currentNode = list(filter(lambda x: x.name == name, currentNode.children))[0]
                # if name not in [child.name for child in currentNode.children]:
                index = index + 1
            elif line[2:4] == "ls":
                index = index + 1
                line = lines[index]
                while line[0] != "$" and index < len(lines):
                    [first, second] = line.split(" ")[0:2]
                    if first == "dir":
                        newNode = node(second, 0, currentNode, "dir")
                        currentNode.children.append(newNode)
                    else:
                        newNode = node(second, int(first), currentNode, "file")
                        currentNode.children.append(newNode)
                    index = index + 1
                    if (index >= len(lines)):
                        break
                    line = lines[index]
totalSize = nodeSize(root)
findSmallNodes(root)
print(smallNodes)

unusedSpace = 70000000 - totalSize
spaceNeeded = 30000000 - unusedSpace
findDirectoryToDelete(root, spaceNeeded)
print(minSizeSoFar)