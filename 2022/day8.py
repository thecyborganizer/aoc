trees = []
with open("day8input.txt") as f:
    trees = [[int(y) for y in list(x.strip())] for x in f.readlines()]

w = len(trees[0])
h = len(trees)
visible = [[False for _ in range(w)] for _ in range(h)]
score = [[0 for _ in range(w)] for _ in range(h)]

count = 0
maxScore = 0
for i in range(h):
    for j in range(w):
        height = trees[i][j]
        left = trees[i][0:j]
        right = trees[i][j+1:]
        up = [trees[x][j] for x in range(i)]
        down = [trees[x][j] for x in range(i+1, h)]
        if len(list(filter(lambda x: x >= height, left))) == 0 or len(list(filter(lambda x: x >= height, right))) == 0 or len(list(filter(lambda x: x >= height, up))) == 0 or len(list(filter(lambda x: x >= height, down))) == 0:
            count = count + 1
        left.reverse()
        scoreRight = next((y+1 for y, x in enumerate(right) if x >= height), len(right))
        scoreLeft = next((y+1 for y, x in enumerate(left) if x >= height), len(left))
        up.reverse()
        scoreUp = next((y+1 for y, x in enumerate(up) if x >= height), len(up))
        scoreDown = next((y+1 for y, x in enumerate(down) if x >= height), len(down))
        score = scoreLeft * scoreRight * scoreUp * scoreDown
        if score > maxScore:
            maxScore = score




print(count)
print(maxScore)