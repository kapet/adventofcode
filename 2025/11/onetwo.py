import heapq

data = {}
for l in open("2025/11/input.txt"):
    name, l = l.split(":")
    targets = l.strip().split()
    assert name not in data
    assert len(targets) == len(set(targets))
    data[name] = targets

# There are only ~600 nodes, the complexity is not in the number of
# nodes but in the many possible paths.
# Assumption: the graph has no cycles.
# Finding out the number of connections to the end node is easy for
# every node directly connected to the end node - it's just 1.
# The next nodes down all have a distance of 2, and so on.
# The idea is to do a DFS and then calculate the number of paths
# between a node to the end node ON THE WAY BACKWARDS.
# Once all nodes have been looked at, the start node has the result.

def all_paths(start, finish):
    paths = {}
    stack = [(0, start)] # on start node, 0 steps walked
    # need a max heap so steps are all with a negative sign.
    # This way we always look at the deepest path, do a DFS.
    while stack:
        steps, node = stack[0] # do not pop yet!
        p = 0
        try_again = False
        for target in data[node]:
            if target == finish:
                p += 1
            elif target == "out":
                # happens in part two, is a dead end
                p += 0
            elif target in paths:
                p += paths[target]
            else:
                # found a next node we have no data for yet
                heapq.heappush(stack, (steps-1, target))
                try_again = True
        if not try_again:
            # all next nodes had data so we have a result and can
            # drop the current node from the heap
            heapq.heappop(stack)
            assert node not in paths
            paths[node] = p
    return paths[start]

print("one", all_paths("you", "out"))

# At the DAC and FFT nodes, all paths MUST converge. Split the problem up.

# svr -> dac -> fft -> out
sd = all_paths("svr", "dac")
df = all_paths("dac", "fft")
fo = all_paths("fft", "out")
# svr -> fft -> dac -> out
sf = all_paths("svr", "fft")
fd = all_paths("fft", "dac")
do = all_paths("dac", "out")
print("two", sd*df*fo + sf*fd*do)