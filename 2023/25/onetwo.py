import collections
import random

connections = collections.defaultdict(set)
for line in open('2023/25/input.txt'):
    line = line.split()
    src = line[0][:-1]
    for dst in line[1:]:
        connections[src].add(dst)
        connections[dst].add(src)

def karger(graph):
    nodes = {key: 1 for key in graph.keys()}
    edges = [((src, dst), src+dst) for src, dests in graph.items() for dst in dests if src < dst]

    while len(nodes) > 2:
        weights = [2/(nodes[a]+nodes[b]) for (a,b),_ in edges]
        (n1, n2), _ = random.choices(edges, weights=weights, k=1)[0]
        n3 = n1+n2  # string concat
        nodes[n3] = nodes.pop(n1) + nodes.pop(n2)

        new_edges = []
        for edge, name in edges:
            if n1 in edge and n2 in edge:
                pass
            elif n1 in edge or n2 in edge:
                e = set(edge)
                e.add(n3)
                e.discard(n1)
                e.discard(n2)
                s,d = sorted(e)
                new_edges.append(((s,d), name))
            else:
                new_edges.append((edge, name))
        edges = new_edges
    
    return [name for _,name in edges], nodes.values()

edges = []
while len(edges) != 3:
    edges, nodes = karger(connections)
    print(len(edges), edges, nodes)
nodes = list(nodes)
print('one:', nodes[0]*nodes[1])
