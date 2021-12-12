import collections

edges = [l.strip().split('-') for l in open('2021/12/input.txt')]

nodes = {}
for n1, n2 in edges:
    # don't include edges going 'back' to start
    if n2 != 'start':
        nodes.setdefault(n1, set()).add(n2)
    if n1 != 'start':
        nodes.setdefault(n2, set()).add(n1)

small_caves = [n for n in nodes.keys() if n.islower()]

visited = collections.defaultdict(int)
small_twice = False
paths_found = 0

def visit(path, node):
    global small_twice, paths_found

    visited[node] += 1

    if node in small_caves and small_twice and visited[node] > 1:
        # already visited some cave twice, illegal to visit this one again
        pass

    else:
        path.append(node)

        if node == 'end':
            print(','.join(path))
            paths_found += 1

        else:
            set_twice = False
            if node in small_caves and visited[node] > 1:
                # second time we see this small cave! set flag
                small_twice = True
                set_twice = True

            # try visit all nodes connected to this one
            for child in nodes[node]:
                visit(path, child)

            if set_twice:
                small_twice = False

        path.pop()

    visited[node] -= 1

visit([], 'start')

print('total {} paths found'.format(paths_found))