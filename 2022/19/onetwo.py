class rvector:
    def __init__(self, ore, clay, obsidian, geode):
        self.o = ore
        self.c = clay
        self.b = obsidian
        self.g = geode

    @classmethod
    def fromtuple(cls, tpl):
        return cls(tpl[0], tpl[1], tpl[2], tpl[3])

    def astuple(self):
        return (self.o, self.c, self.b, self.g)

    def __repr__(self) -> str:
        return str(self.astuple())

    def __eq__(self, other):
        return self.o==other.o and self.c==other.c and self.b==other.b and self.g==other.g

    def __hash__(self):
        return hash((self.o, self.c, self.b, self.g))

    def __add__(self, other):
        return rvector(self.o+other.o, self.c+other.c, self.b+other.b, self.g+other.g)

    def __sub__(self, other):
        return rvector(self.o-other.o, self.c-other.c, self.b-other.b, self.g-other.g)

    def __ge__(self, other):
        return self.o>=other.o and self.c>=other.c and self.b>=other.b and self.g>=other.g

    def __lt__(self, other):
        return not self.__ge__(other)


class simstack:
    def __init__(self):
        self.seen = set()
        self.new_stack = []
        self.add(rvector(1,0,0,0), rvector(0,0,0,0), rvector(0,0,0,0))
        self.swap()

    def add(self, robots, materials, old_materials):
        if (robots, materials) not in self.seen:
            self.seen.add((robots, materials))
            self.new_stack.append((robots, materials, old_materials))

    def swap(self):
        self.stack = self.new_stack
        self.new_stack = []


robot_index = (rvector(1,0,0,0), rvector(0,1,0,0), rvector(0,0,1,0), rvector(0,0,0,1))

def sim(blueprint):
    stack = simstack()
    for minute in range(24):
        for robots, materials, old_materials in stack.stack:
            new_materials = materials + robots

            skipped = 0
            for index, required in zip(robot_index, blueprint):
                if materials >= required:
                    if old_materials < required:
                        remaining = new_materials - required
                        grown = robots + index
                        stack.add(grown, remaining, rvector(0,0,0,0))
                    else:
                        skipped += 1

            if skipped < 4:
                stack.add(robots, new_materials, materials)

        stack.swap()
        print('after', minute+1, ':', len(stack.stack)) #, '=>', stack.stack)

    k = max(stack.stack, key=lambda x: x[1].g)
    return k


blueprints = []
for line in open('2022/19/test.txt'):
    line = line.split()
    ore = rvector(int(line[6]), 0, 0, 0)
    clay = rvector(int(line[12]), 0, 0, 0)
    obsidian = rvector(int(line[18]), int(line[21]), 0, 0)
    geode = rvector(int(line[27]), 0, int(line[30]), 0)
    blueprints.append((ore, clay, obsidian, geode))


print(blueprints[1])
print(sim(blueprints[1]))

if 0:
    results = [sim(t) for t in blueprints]
    print(results[0])
    print('one:', max(results))
