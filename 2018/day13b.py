import numpy as np
from enum import Enum

def rotate_left(direction):
    return (direction - 1) % 4

def rotate_right(direction):
    return (direction + 1) % 4

north, east, south, west = range(4)

horizontal, vertical, intersection, nw_se_curve, sw_ne_curve = range(1,6)

left, straight, right = range(-1, 2)

#text = [list(x) for x in open('day13test2.txt', 'r')]
#text = [list(x) for x in open('day13test.txt', 'r')]
text = [list(x) for x in open('day13input.txt', 'r')]

def print_grid(g, carts):
    cart_positions = carts.keys()
    for j in range(np.size(g, 0)):
        for i in range(np.size(g, 1)):
            c = " "
            if (i, j) in cart_positions:
                if carts[(i,j)][0] == north:
                    c = "^"
                elif carts[(i,j)][0] == east:
                    c = ">"
                elif carts[(i,j)][0] == south:
                    c = "v"
                elif carts[(i,j)][0] == west:
                    c = "<"
                else:
                    print("wtf")
                    return
            elif g[j, i] == horizontal:
                c = "-"
            elif g[j,i] == vertical:
                c = "|"
            elif g[j,i] == intersection:
                c = "+"
            elif g[j,i] == nw_se_curve:
                c = "\\"
            elif g[j,i] == sw_ne_curve:
                c = "/"
            print(c, end="")
        print("")
            

grid = np.zeros((len(text), len(text[0])), dtype=int)
carts = {}
for j in range(len(text)):
    for i in range(len(text[0])):
        print(i, j)
        #print(text[j])
        c = text[j][i]
        val = 0
        if c == '-':
            val = horizontal
        elif c == '|':
            val = vertical
        elif c == '+':
            val = intersection
        elif c == '/':
            val = sw_ne_curve
        elif c == '\\':
            val = nw_se_curve
        elif c == '>':
            val = horizontal
            carts[(i,j)] = (east, left)
        elif c == '<':
            val = horizontal
            carts[(i,j)] = (west, left)
        elif c == '^':
            val = vertical
            carts[(i,j)] = (north, left)
        elif c == 'v':
            val = vertical
            carts[(i,j)] = (south, left)
        grid[j, i] = val

t = 0
collision = False
while len(carts.keys()) > 1:
    t += 1
    print(t)
    cart_positions = sorted(carts.keys(), key = lambda x: (x[1], x[0]))
    #print(cart_positions)
    num_carts = len(cart_positions)
    i = 0
    has_moved = set()
    while i < num_carts:
        #print(i, num_carts)
        cart_position = cart_positions[i]
        if cart_position not in carts:
            i += 1
        else:
            cart = carts[cart_position]
            #print(cart_position, cart)
            pos = (0,0)
            if cart[0] == north:
                pos = (cart_position[0], cart_position[1] - 1)
            elif cart[0] == east:
                pos = (cart_position[0] + 1, cart_position[1])
            elif cart[0] == south:
                pos = (cart_position[0], cart_position[1] + 1)
            elif cart[0] == west:
                pos = (cart_position[0] - 1, cart_position[1])
            #print(pos)
            val = grid[pos[1], pos[0]]
            #print(val)
            dir = carts[cart_position][0]
            had_intersection = False
            if val == nw_se_curve:
                if dir == east or dir == west:
                    dir = rotate_right(dir) # right turn
                else:
                    dir = rotate_left(dir) # left turn
            if val == sw_ne_curve:
                if dir == east or dir == west:
                    dir = rotate_left(dir)
                else:
                    dir = rotate_right(dir)
            elif val == intersection:
                dir = (dir + carts[cart_position][1]) % 4
                had_intersection = True
                #print("cart hit intersection")
            if pos in carts.keys():
                collision = True
                #print("Found collision")
                #print(pos)
                del carts[cart_position]
                del carts[pos]
                #print(carts)
                #if pos in has_moved:
                #    num_carts -= 1
                #else:
                #    num_carts -= 2
            else:
                intersection_state = carts[cart_position][1]
                if had_intersection:
                    intersection_state = ((intersection_state + 2) % 3) - 1
                del carts[cart_position]
                carts[pos] = (dir, intersection_state)
                has_moved.add(pos)
                #print(carts)
                i += 1
    #print_grid(grid, carts)
print(carts)