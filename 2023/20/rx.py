import collections

configs = {}
for line in open('2023/20/input.txt'):
    line = line.split()
    name = line[0]
    if name == 'broadcaster':
        type_ = 'b'
    else:
        type_ = name[0]
        name = name[1:]
    destinations = tuple(d.strip(',') for d in line[2:])
    configs[name] = (type_, destinations)

inputs = collections.defaultdict(list)
for name, (_, destinations) in configs.items():
    for dest in destinations:
        inputs[dest].append(name)

with open('2023/20/rx.dot', 'w') as outfile:
    outfile.write('digraph G {\n')
    heap = ['rx']
    nodes = set()
    while heap:
        name = heap.pop(0)
        if name in nodes:
            continue
        nodes.add(name)
        if name == 'broadcaster':
            continue
        for src in inputs[name]:
            outfile.write(f'  {src} -> {name};\n')
            heap.append(src)
    for name in nodes:
        type_ = configs.get(name, [None])[0]
        if type_ == 'b' or name == 'rx':
            outfile.write(f'  {name} [shape=square];\n')
        elif type_ == '&':
            outfile.write(f'  {name} [shape=diamond];\n')
    outfile.write('}\n')
