import collections

class rvector(collections.namedtuple('rvector', ['ore', 'clay', 'obsidian', 'geode'])):
    __slots__ = () # no extra attributes, save memory

    def __add__(self, other):
        return rvector(*[self[i]+other[i] for i in range(4)])

    def __sub__(self, other):
        return rvector(*[self[i]-other[i] for i in range(4)])

    def __mul__(self, other):
        assert type(other) is int
        return rvector(*[self[i]*other for i in range(4)])

    def __and__(self, other):
        return rvector(*[(other[i]>0) and self[i] or 0 for i in range(4)])
        
    def __ge__(self, other):
        return all([self[i]>=other[i] for i in range(4)])

    def __lt__(self, other):
        return not self.__ge__(other)

t0 = rvector(1,2,3,4)
assert t0[1] == 2
t1 = t0 + rvector(5,6,7,8)
assert t1[1] == 8
assert t1 >= t0
assert not (t0 >= t1)
assert t0 < t1
t1 = t0 * 2
assert t1[1] == 4
t1 = rvector(1,2,3,4)
assert t0 == t1
t1 = t0 & rvector(0,1,0,0)
assert t1[0] == 0
assert t1[1] == 2

# Fundamentally this is a typical tree evaluation with the need to figure out ways
# to quickly predict which branches can be dropped. The problem is that it's quite
# hard in this case to find a simple way to do that. This solution applies a variety
# of methods and still takes a few minutes to run:
# - Drop branches that build more robots than needed to mine enough resources.
# - Drop branches that do not build robots at the earliest opportunity.
# - Drop branches that have fallen behind on the potential number of geodes.
# - Drop branches that build a robot in the last minute.

# More ideas to consider:
# - DFS instead of round-based, might make it easier to cull based on potential.
# - Check with Python profiler what is taking so long.
# - Move test for potential before it's added to the stack.
# - Try a {potential: {robots: [material, material, ...]}} stack.
# - Don't build anything but geode robots in the second-last round.

robot_index = (rvector(1,0,0,0), rvector(0,1,0,0), rvector(0,0,1,0), rvector(0,0,0,1))

def sim(minutes, blueprint):
    stack = [(rvector(1,0,0,0), rvector(0,0,0,0), rvector(0,0,0,0))]
    for minute in range(minutes, 0, -1):
        print('.', end='', flush=True)
        new_stack = []
        min_potential = 0

        # it makes no sense to produce more than what we could use in the remaining time
        max_resources = [b*minute for b in blueprint] # max per robot
        max_resources = rvector(*[max([t[i] for t in max_resources]) for i in range(3)], 9999)

        for robots, materials, old_materials in stack:
            new_materials = materials + robots
            potential = materials.geode + minute
            if potential < min_potential:
                continue
            min_potential = potential

            skipped = 0
            if minute > 1: # not useful in last minute as they wont produce anything
                for index, required in zip(robot_index, blueprint):
                    if (new_materials&index) >= (max_resources&index):
                        # already have enough resources, dont build more of this robot type
                        continue
                    if materials >= required:
                        if old_materials < required:
                            remaining = new_materials - required
                            grown = robots + index
                            new_stack.append((grown, remaining, rvector(0,0,0,0)))
                        else:
                            skipped += 1

            if skipped < 4:
                new_stack.append((robots, new_materials, materials))

        stack = new_stack

    k = max([t[1].geode for t in stack])
    print('  ->', k)
    return k


blueprints = []
for line in open('2022/19/input.txt'):
    line = line.split()
    ore = rvector(int(line[6]), 0, 0, 0)
    clay = rvector(int(line[12]), 0, 0, 0)
    obsidian = rvector(int(line[18]), int(line[21]), 0, 0)
    geode = rvector(int(line[27]), 0, int(line[30]), 0)
    blueprints.append((ore, clay, obsidian, geode))


results = [sim(24, t) for t in blueprints]
quality = sum((i+1)*v for i,v in enumerate(results))
print('one:', quality)

blueprints = blueprints[:3]
results = [sim(32, t) for t in blueprints]
if len(results) == 3:
    print('two:', results[0] * results[1] * results[2])
else:
    print(results)
