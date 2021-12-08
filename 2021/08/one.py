class Entry:
    def __init__(self, line):
        line = line.split()
        self.patterns = line[:10]
        self.outputs = line[11:]

data = [Entry(line) for line in open('2021/08/input.txt')]

total = 0
for e in data:
    for out in e.outputs:
        if len(out) in (2,3,4,7):
            total += 1

print(total)