edges = [l.strip().split('-') for l in open('2021/12/input.txt')]

nodes = {}
for n1, n2 in edges:
    nodes.setdefault(n1, set()).add(n2)
    nodes.setdefault(n2, set()).add(n1)

small_caves = [n for n in nodes.keys() if n.islower()]

visited = set()
paths_found = 0

def visit(path, node):
    global paths_found

    path.append(node)
    if node in small_caves:
        visited.add(node)

    if node == 'end':
        print(','.join(path))
        paths_found += 1
    else:
        for child in nodes[node]:
            if child not in visited:
                visit(path, child)

    path.pop()
    visited.discard(node)

visit([], 'start')

print('total {} paths found'.format(paths_found))