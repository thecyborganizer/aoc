import re
import itertools
import numpy
import math

moons = []

seen = set()

def lcm(a,b): 
    return abs(a * b) // math.gcd(a,b)

class planet:

    def __init__(self, positions):
        self.x, self.y, self.z = map(lambda x: int(x), positions)
        self.vx, self.vy, self.vz = 0, 0, 0
    
    def __str__(self):
        return ",".join([str(self.x), str(self.y), str(self.z)]) + ":" + ",".join([str(self.vx), str(self.vy), str(self.vz)])

    def __repr__(self):
        return ",".join([str(self.x), str(self.y), str(self.z)]) + ":" + ",".join([str(self.vx), str(self.vy), str(self.vz)])


    def update_position_x(self):
        self.x += self.vx
    
    def update_position_y(self):
        self.y += self.vy
    
    def update_position_z(self):
        self.z += self.vz

    def energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return potential * kinetic

    def key_x(self):
        return (self.x, self.vx)
    def key_y(self):
        return (self.y, self.vy)
    def key_z(self):
        return (self.z, self.vz)

    def key(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)

def apply_gravity_x(m1, m2):
    if m1.x < m2.x:
        m1.vx += 1
        m2.vx -= 1
    elif m1.x > m2.x:
        m1.vx -= 1
        m2.vx += 1

def apply_gravity_y(m1, m2):
    if m1.y < m2.y:
        m1.vy += 1
        m2.vy -= 1
    elif m1.y > m2.y:
        m1.vy -= 1
        m2.vy += 1
        
def apply_gravity_z(m1, m2):
    if m1.z < m2.z:
        m1.vz += 1
        m2.vz -= 1
    elif m1.z > m2.z:
        m1.vz -= 1
        m2.vz += 1


#with open("12test.txt") as f:
#with open("12test2.txt") as f:
with open("12input.txt") as f:
    moons = [planet(tuple(re.findall('-*[0-9]+', x))) for x in f.readlines()]


combos = []
for ms in itertools.combinations(moons, 2):
    combos.append(ms)

startx = moons[0].key_x() + moons[1].key_x() + moons[2].key_x() + moons[3].key_x()
x_time = 0
while True:
    for c in combos:
        apply_gravity_x(c[0], c[1])

    for m in moons:
        m.update_position_x()
    state = moons[0].key_x() + moons[1].key_x() + moons[2].key_x() + moons[3].key_x()
    x_time += 1
    if state == startx:
        break

starty = moons[0].key_y() + moons[1].key_y() + moons[2].key_y() + moons[3].key_y()
y_time = 0
while True:
    for c in combos:
        apply_gravity_y(c[0], c[1])

    for m in moons:
        m.update_position_y()
    state = moons[0].key_y() + moons[1].key_y() + moons[2].key_y() + moons[3].key_y()
    y_time += 1
    if state == starty:
        break

startz = moons[0].key_z() + moons[1].key_z() + moons[2].key_z() + moons[3].key_z()
z_time = 0
while True:
    for c in combos:
        apply_gravity_z(c[0], c[1])

    for m in moons:
        m.update_position_z()
    state = moons[0].key_z() + moons[1].key_z() + moons[2].key_z() + moons[3].key_z()
    z_time += 1
    if state == startz:
        break
#print(x_time*y_time*z_time)
for m in moons:
    print(m)
print(lcm(lcm(x_time, y_time), lcm(y_time, z_time)))
# energy = 0
# for m in moons:
#     energy += m.energy()
#     print(m, m.energy())

# print(energy)