import re
import itertools

moons = []



class planet:

    def __init__(self, positions):
        self.x, self.y, self.z = map(lambda x: int(x), positions)
        self.vx, self.vy, self.vz = 0, 0, 0
    
    def __str__(self):
        return ",".join([str(self.x), str(self.y), str(self.z)]) + ":" + ",".join([str(self.vx), str(self.vy), str(self.vz)])


    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return potential * kinetic

def apply_gravity(m1, m2):
        if m1.x < m2.x:
            m1.vx += 1
            m2.vx -= 1
        elif m1.x > m2.x:
            m1.vx -= 1
            m2.vx += 1

        if m1.y < m2.y:
            m1.vy += 1
            m2.vy -= 1
        elif m1.y > m2.y:
            m1.vy -= 1
            m2.vy += 1
        
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

time = 1000
for t in range(time):
    for ms in itertools.combinations(moons, 2):
        apply_gravity(ms[0], ms[1])
    for m in moons:
        m.update_position()

energy = 0
for m in moons:
    energy += m.energy()
    print(m, m.energy())

print(energy)