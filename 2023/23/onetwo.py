import collections
import dataclasses

@dataclasses.dataclass(frozen=True)
class Vector:
    y: int
    x: int

    def __add__(self, other):
        return Vector(self.y+other.y, self.x+other.x)

_maze = [line.strip() for line in open('2023/23/input.txt')]
def maze(loc):
    return _maze[loc.y][loc.x]
height = len(_maze)
width = len(_maze[0])

start = Vector(0, 1)
end = Vector(height-1, width-2)
assert maze(start) == maze(end) == '.'

directions = '><v^'
possible_steps = (
    (Vector( 0, 1), '>'),
    (Vector( 0,-1), '<'),
    (Vector( 1, 0), 'v'),
    (Vector(-1, 0), '^')
)

# STEP 1: convert maze into a graph
# The maze has many steps between few junctions, so this simplifies the later
# path finding work.
nodes = set([start])
edges = set()
to_visit = [(start, start+Vector(1, 0))]
while to_visit:
    first, pos = to_visit.pop(0)
    steps = 0
    previous = first
    blocked_forward = blocked_backwards = False

    while True:
        steps += 1
        if pos == end:
            assert not blocked_backwards
            edges.add((first, pos, steps, blocked_forward))
            break

        next_steps = []
        for inc, direction in possible_steps:
            new = pos + inc
            if maze(new) != '#' and new != previous:
                next_steps.append((new, direction))
        if not next_steps:
            # dead end!
            break
        if len(next_steps) > 1:
            # found a new node
            if blocked_backwards:
                edges.add((pos, first, steps, True))
            else:
                edges.add((first, pos, steps, blocked_forward))
            if pos not in nodes:
                for new, _ in next_steps:
                    to_visit.append((pos, new))
                nodes.add(pos)
            break
        else:
            # path continues
            new, direction = next_steps[0]
            if maze(pos) in directions:
                if maze(pos) == direction:
                    blocked_forward = True
                else:
                    blocked_backwards = True
            previous, pos = pos, new

# STEP 2: graph cleanup

# Convert set of nodes into list, ensure start is first and end is last.
# Will use the index in this list as the node ID, for speed reasons.
nodes = list(nodes)
nodes.remove(start)
nodes.insert(0, start)
nodes.append(end)

start = nodes.index(start)
end = nodes.index(end)
assert start == 0
assert end == len(nodes)-1

# Build complete outgoing edge lists for all nodes. 
undirected_graph = collections.defaultdict(list)
directed_graph = collections.defaultdict(list)
for src, dest, steps, oneway in edges:
    src = nodes.index(src)
    dest = nodes.index(dest)
    undirected_graph[src].append((dest, steps))
    undirected_graph[dest].append((src, steps))
    directed_graph[src].append((dest, steps))
    if not oneway:
        directed_graph[dest].append((src, steps))

assert len(undirected_graph[start]) == 1
assert len(directed_graph[start]) == 1

# STEP 3: calculate longest path using exhaustive DFS
# Optimized for speed as the problem is IIUC NP-hard.

def longest_path(graph):
    visited_root = set()  # ChainMap is more elegant but much slower
    heap = []

    # There can only be one edge that leaves start, so actually
    # begin at the next node.
    pos, steps = graph[start][0]
    heap.append((pos, steps, visited_root))
    visited_root.add(start)

    # There can only be one edge that reaches the end, so only try to
    # get to this node.
    for k,v in graph.items():
        for n,s in v:
            if n == end:
                pre_end, end_steps = k, s
                break
        else:
            continue
        break

    maxlen = 0
    while heap:
        pos, steps, visited = heap.pop()
        visited.add(pos)

        for next_node, next_steps in graph[pos]:
            if next_node in visited:
                # this is very often true, checked first for speed reasons
                pass
            elif next_node == pre_end:
                # as we may not visit the same node twice, we must go to the
                # end once we visit the only pre-end node
                maxlen = max(maxlen, steps+next_steps+end_steps)
            else:
                heap.append((next_node, steps+next_steps, visited.copy()))
    return maxlen

import time
t0 = time.time()
print('one:', longest_path(directed_graph))
print('two:', longest_path(undirected_graph))
t1 = time.time()
print('duration:', t1-t0)
