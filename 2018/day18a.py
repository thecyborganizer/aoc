import itertools

dirs = set(list(itertools.product([-1, 0, 1], [-1, 0, 1])))
dirs.remove((0, 0))
dirs = list(dirs)
print(dirs)

def get_neighbors(x, y):
    global dirs
    global size
    to_return = []
    for d in dirs:
        eval_x = x + d[0]
        eval_y = y + d[1]
        if eval_x < 0 or eval_x >= size or eval_y < 0 or eval_y >= size:
            continue
        to_return.append((eval_x, eval_y))
    return to_return

def update_space(grid, next_step, x, y):
    neighbors = get_neighbors(x, y)
    tree_count = 0
    lumber_count = 0
    for n in neighbors:
        if grid[n[1]][n[0]] == '|':
            tree_count += 1
        elif grid[n[1]][n[0]] == '#':
            lumber_count += 1
    if grid[y][x] == '.':
        if tree_count >= 3:
            next_step[y][x] = '|'
        else:
            next_step[y][x] = '.'
    elif grid[y][x] == '|':
        if lumber_count >= 3:
            next_step[y][x] = '#'
        else:
            next_step[y][x] = '|'
    elif grid[y][x] == '#':
        if tree_count >= 1 and lumber_count >= 1:
            next_step[y][x] = '#'
        else:
            next_step[y][x] = '.'
def score(grid):
    lumber_count = 0
    tree_count = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == "#":
                lumber_count += 1
            elif grid[y][x] == "|":
                tree_count += 1
    return lumber_count, tree_count

#grid = [list(x.rstrip()) for x in open('day18test.txt', 'r')]
grid = [list(x.rstrip()) for x in open('day18input.txt', 'r')]
size = len(grid)
for g in grid:
    print("".join(g))

next_step = [[""]*size for x in range(size)]

for t in range(1, 2000):
    for y in range(size):
        for x in range(size):
            update_space(grid, next_step, x, y)
    grid = next_step
    next_step = [[""]*size for x in range(size)]
    if t > 1000:
        totals = score(grid)
        print(t, ",", totals[0], ",", totals[1])

# for g in grid:
#     print("".join(g))


#print(lumber_count, tree_count, lumber_count*tree_count)