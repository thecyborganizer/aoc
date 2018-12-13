import numpy as np
from enum import Enum

north, east, south, west = range(4)

horizontal, vertical, intersection, nw_se_curve, sw_ne_curve = range(1,6)

left, straight, right = range(-1, 2)

text = [list(x) for x in open('day13test.txt', 'r')]

grid = np.zeros((len(text), len(text[0])), dtype=int)
carts = []
for j in range(len(text)):
    for i in range(len(text[0])):
        print(i, j)
        print(text[j])
        c = text[j][i]
        val = 0
        if c == '-':
            val = horizontal
        elif c == '|':
            val = vertical
        elif c == '+':
            val = intersection
        elif c == '/':
            val = nw_se_curve
        elif c == '\\':
            val = sw_ne_curve
        elif c == '>':
            val = horizontal
            carts.append((i, j, east, left))
        elif c == '<':
            val = horizontal
            carts.append((i, j, west, left))
        elif c == '^':
            val = vertical
            carts.append((i, j, north, left))
        elif c == 'v':
            val = vertical
            carts.append((i, j, south, left))
        grid[j, i] = val

t = 0
collision = False
while not collision:
    carts = sorted(carts, key = lambda x: (x[1], x[0]))
    print(carts)
    cart_positions = set()
    for i in range(len(carts)):
        cart = carts[i]
        pos = (0,0)
        if cart[2] == north:
            pos = (cart[0], cart[1] - 1)
        elif cart[2] == east:
            pos = (cart[0] + 1, cart[1])
        elif cart[2] == south:
            pos = (cart[0], cart[1] + 1)
        elif cart[2] == west:
            pos = (cart[0] - 1, cart[1])
        print(pos)
        val = grid[pos[1], pos[0]]
        print(val)
        dir = cart[2]
        had_intersection = False
        if val == nw_se_curve:
            if dir == east or dir == west:
                dir = (dir + 1) % 4 # right turn
            else:
                dir = (dir - 1) % 4 # left turn
        if val == sw_ne_curve:
            if dir == east or dir == west:
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4
        elif val == intersection:
            dir = (dir + cart[3]) % 4
            had_intersection = True
            print("cart hit intersection")
        if had_intersection:
            intersection_state = ((cart[3] + 2) % 3) - 1
            carts[i] = (pos[0], pos[1], dir, intersection_state)
        else:
            carts[i] = (pos[0], pos[1], dir, cart[3])
        if pos in cart_positions:
            collision = True
            print("Found collision")
            print(pos)
        else:
            cart_positions.add(pos)
print(carts)