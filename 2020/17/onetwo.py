import collections
import itertools

infile = '2020/17/input.txt'

class PocketDimension:
    def __init__(self, dim):
        self.mins = [0]*dim
        self.maxs = [0]*dim
        self.map = collections.defaultdict(int)
        self.dim = dim

    def getval(self, vec):
        return self.map[vec]
    
    def sumneighbors(self, vec):
        s = 0
        targets = [range(t-1, t+2) for t in vec]
        for t in itertools.product(*targets):
            if t != vec:
                s += self.map[t]
        return s

    def setval(self, vec):
        for i, v in enumerate(vec):
            self.mins[i] = min(self.mins[i], v)
            self.maxs[i] = max(self.maxs[i], v)
        self.map[vec] = 1

    def iterate(self):
        newpd = PocketDimension(self.dim)
        targets = [range(self.mins[t]-1, self.maxs[t]+2) for t in range(self.dim)]
        for t in itertools.product(*targets):
            s = self.sumneighbors(t)
            if self.getval(t):
                if 2 <= s <= 3:
                    newpd.setval(t)
            else:
                if s == 3:
                    newpd.setval(t)
        return newpd


pd3 = PocketDimension(3)
pd4 = PocketDimension(4)

for y, l in enumerate(open(infile)):
    for x, c in enumerate(l.strip()):
        if c == '#':
            pd3.setval((0, y, x))
            pd4.setval((0, 0, y, x))

for _ in range(6):
    pd3 = pd3.iterate()
    pd4 = pd4.iterate()
print('one', sum(pd3.map.values()))
print('two', sum(pd4.map.values()))
