#import numpy as np
from collections import defaultdict
import itertools
grid = [list(x.rstrip()) for x in open('day15input.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test2.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test3.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test4.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test5.txt', 'r')]
#grid = [list(x.rstrip()) for x in open('day15test6.txt', 'r')] #failing!
#grid = [list(x.rstrip()) for x in open('15.inp', 'r')]
#grid = [list(x.rstrip()) for x in open('bizarre_edge_case.txt', 'r')]

#grid = np.zeros((len(text), len(text[0])), dtype="char")

def get_adjacent_spaces(p):
    diffs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    to_return = []
    for d in diffs:
        to_return.append((p[0] + d[0], p[1] + d[1]))
    return to_return

def get_adjacent_empty_spaces(p):
    global goblins
    global elves
    global walls
    #diffs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    to_return = []
    for n in get_adjacent_spaces(p):
        if n not in goblins.keys() and n not in elves.keys() and n not in walls:
            to_return.append(n)
    return to_return

def print_grid(g, format_like_aoc):
    global goblins
    global elves
    global walls
    for j in range(len(g)):
        #print(j)
        elves_to_print = []
        goblins_to_print = []
        for i in range(len(g[0])):
            char = ""
            if (i, j) in goblins.keys():
                char = "G"
                goblins_to_print.append("G(" + str(goblins[(i, j)]) + ")")
            elif (i, j) in elves.keys():
                char = "E"
                elves_to_print.append("E(" + str(elves[(i, j)]) + ")")
            elif (i, j) in walls:
                char = "#"
            else:
                char = "."
            print(char, end="")
        if format_like_aoc:
            print (" " + ",".join(goblins_to_print) + " " + ",".join(elves_to_print), end="")
        print("")

def get_squares_in_range(p, s):
    global goblins
    global elves
    global walls
    to_return = []
    diffs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for d in diffs:
        square = (p[0] + d[0], p[1] + d[1])
        if square == s:
            to_return.append(square)
        elif square not in goblins.keys() and square not in elves.keys() and square not in walls:
            to_return.append(square)
    return to_return

def connected_nodes(p, seen):
    global goblins
    global elves
    global walls
    seen.add(p)
    diffs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for d in diffs:
        next = (p[0] + d[0], p[1] + d[1])
        #print(next, grid[next[1]][next[0]])
        if next not in seen and next not in goblins.keys() and next not in elves.keys() and next not in walls:
            more = connected_nodes(next, seen)
            seen |= more
    return seen

def distance(start, goal):
    return abs(start[1] - goal[1]) + abs(start[0] - goal[0])

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path

def a_star(start, goal):
    global grid
    global goblins
    global elves
    global walls
    #diffs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    diffs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    #diffs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    closed_set = set()
    open_set = set()
    open_set.add(start)
    came_from = {}
    gScore = defaultdict(lambda: 9999999999)
    gScore[start] = 0
    fScore = defaultdict(lambda: 9999999999)
    fScore[start] = distance(start, goal)

    while len(open_set) != 0:
        current = (-1, -1)
        min_val = 99999999
        for node in open_set:
            if fScore[node] < min_val:
                current = node
                min_val = fScore[node]
            elif fScore[node] == min_val:
                if node[1] < current[1]:
                    current = node
                    min_val = fScore[node]
                elif node[1] == current[1] and node[0] < current[0]:
                    current = node
                    min_val = fScore[node]
        if current == goal:
            return reconstruct_path(came_from, current)
            #return(gScore[current])
            # done
        open_set.remove(current)
        closed_set.add(current)
        for d in diffs:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if neighbor in closed_set or neighbor in goblins.keys() or neighbor in elves.keys() or neighbor in walls:
                continue
            tentative_gscore = gScore[current] + 1 # fixed dist
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_gscore >= gScore[neighbor]:
                continue
            came_from[neighbor] = current
            gScore[neighbor] = tentative_gscore
            fScore[neighbor] = gScore[neighbor] + distance(neighbor, goal)

def reading_order(p1, p2):
    if p1[1] < p2[1]:
        return True
    if p1[1] == p2[1] and p1[0] < p2[0]:
        return True
    return False

goblins = {}
elves = {}
walls = set()
        #TODO REMOVE
        #if (i,j) == (19, 11):
        #    elves[(i,j)] = 2


#print(get_squares_in_range((8, 11)))
#print_grid(grid)
#print(grid[1][5])
#print(connected_nodes((9,1), set()))

#print(a_star((8, 20), (8, 22)))
#print(a_star((23,22), (26,22)))
def run_simulation(attack_power):
    global grid
    global goblins
    global elves
    global walls
    goblins = {}
    elves = {}
    walls = set()
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == '#':
                walls.add((i, j))
            elif grid[j][i] == 'G':
                goblins[(i, j)] = 200
            elif grid[j][i] == 'E':
                elves[(i,j)] = 200

    k = 0

    while True:

        print(str(k) + "\t" + str(len(goblins)) + "\t" + str(len(elves)))
        #print_grid(grid, False)
        units = []
        for u in sorted(list(goblins.keys()) + list(elves.keys()), key=lambda element: (element[1], element[0])):
            if u in goblins.keys():
                units.append((u, "G"))
            elif u in elves.keys():
                units.append((u, "E"))
        for unit in units:
            hp = -1
            if unit[0] in goblins.keys():
                hp = goblins[unit[0]]
            elif unit[0] in elves.keys():
                hp = elves[unit[0]]
            #print(unit)
            #print("start\t"+str(unit[0][0] + 1)+"\t"+str(unit[0][1] + 1)+"\t"+unit[1]+"\t"+str(hp))

        #print("round ", k + 1)
        #units = sorted(list(goblins.keys()) + list(elves.keys()), key=lambda element: (element[1], element[0]))
        
        for i in range(len(units)):
            unit = units[i][0]
            enemy_dict = {}
            if unit in goblins.keys() and units[i][1] == "G":
                enemy_dict = elves
            elif unit in elves.keys() and units[i][1] == "E":
                enemy_dict = goblins
            else:
                continue
            squares_in_range = []
            for enemy in enemy_dict.keys():
                squares_in_range.extend(get_squares_in_range(enemy, unit))
            needs_to_move = True
            for s in squares_in_range:
                if distance(unit, s) == 0:
                    needs_to_move = False
                    break
            moved = False
            if needs_to_move:
                reachable = connected_nodes(unit, set())
                fewest_steps = 99999999
                goals = []
                goal_paths = {}
                for s in sorted(squares_in_range, key=lambda element: (element[1], element[0])):
                    if s in reachable:
                        for a in get_adjacent_empty_spaces(unit):
                            shortest_path = a_star(a, s)
                            if shortest_path is not None:
                                steps = len(shortest_path)
                                if steps < fewest_steps:
                                    goals.clear()
                                    fewest_steps = steps
                                    goals.append(s)
                                    goal_paths[s] = shortest_path
                if len(goals) != 0:
                    moved = True
                    goal = sorted(goals, key=lambda e: (e[1], e[0]))[0]
                    new_position = goal_paths[goal][-1]
                    if unit in goblins.keys():
                        goblins[new_position] = goblins[unit]
                        del goblins[unit]
                    else:
                        elves[new_position] = elves[unit]
                        del elves[unit]
            if moved:
                unit = new_position
            #attack
            target = (-1, -1)
            min_hp = 201
            for p in get_adjacent_spaces(unit):
                if p in enemy_dict.keys():
                    if enemy_dict[p] < min_hp or (enemy_dict[p] == min_hp and reading_order(p, target)):
                        target = p
                        min_hp = enemy_dict[p]
            if target != (-1, -1):
                if units[i][1] == "G":
                    enemy_dict[target] -= 3
                elif units[i][1] == "E":
                    enemy_dict[target] -= attack_power
                if enemy_dict[target] <= 0:
                    got_one = True
                    #print("got one")
                    del enemy_dict[target]
        if len(goblins) == 0 or len(elves) == 0:
            print("COMBAT IS OVER")
            total_hp = 0
            if len(goblins) == 0:
                print("ELVES WIN")
                for e in elves.values():
                    total_hp += e
            else:
                print("GOBLINS WIN")
                for g in goblins.values():
                    total_hp += g
            print (k, "*", total_hp)
            print((k) * total_hp)
            if len(elves) == 10:
                return 0
            else:
                return 1
        else:
            k += 1

retval = -1
attack_power = 4
while retval != 0:
    retval = run_simulation(attack_power)
    print(attack_power)
    attack_power += 1
                #if i == len(units) - 1:
                #    print("Killed on last hit, add one")
    #print_grid(grid, False)
    #units = sorted(list(goblins.keys()) + list(elves.keys()), key=lambda element: (element[1], element[0]))
    # for unit in units:
    #     unit_type = ""
    #     hp = -1
    #     if unit in goblins.keys():
    #         unit_type = "G"
    #         hp = goblins[unit]
    #     elif unit in elves.keys():
    #         unit_type = "E"
    #         hp = elves[unit]
    #     else:
    #         unit_type = "!!!!!" 
    #     print("start\t" + str(unit[0] + 1) + "\t" + str(unit[1] + 1) + "\t" + unit_type + "\t" + str(hp))

    #print(goblins)
    #print(elves)