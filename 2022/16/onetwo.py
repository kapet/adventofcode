import itertools
import re

flowrate = {} # valve -> rate
distance = {} # source valve -> destination valve -> distance

m = re.compile(r'Valve (.+?) has flow rate=(\d+); tunnels? leads? to valves? (.+)$')
for line in open('2022/16/input.txt'):
    valve, rate, tunnels = m.match(line).groups()
    rate = int(rate)
    tunnels = tunnels.split(', ')
    assert valve not in flowrate
    flowrate[valve] = rate
    distance[valve] = {target: 1 for target in tunnels}

# calculate shortest paths between all nodes, Floyd-Warshall
nodes = flowrate.keys()
for k in nodes:
    for i in nodes:
        for j in nodes:
            if i == j:
                # don't need to loop back
                continue
            distance[i][j] = min(distance[i].get(j, 999), distance[i].get(k, 999)+distance[k].get(j, 999))

# drop nodes without usable valves, they're included in the distances now
nodes = set(['AA'] + [valve for valve,rate in flowrate.items() if rate > 0])
flowrate = {key:value for key,value in flowrate.items() if key in nodes}
distance = {key:value for key,value in distance.items() if key in nodes}
for valve in distance.keys():
    distance[valve] = {target: dist for target,dist in distance[valve].items() if target in nodes}

########################### ONE

# start iteration:
#   given time left (plus 1 min to 'open' the valve in AA)
#   on node AA
#   0 pressure released
#   no nodes visited yet

def allPaths(max_time):
    stack = [(max_time+1, 'AA', 0, set())]
    results = {}
    while stack:
        time_remaining, valve, released, visited = stack.pop(0)
        visited.add(valve)

        # open this valve, calculate pressure release for remaining time
        time_remaining -= 1
        released += time_remaining * flowrate[valve]

        # remember the best result for this set of visited nodes
        visited_key = frozenset(visited)
        results[visited_key] = max(results.get(visited_key, 0), released)

        # move on to nodes that can be reached within available time
        for target,cost in distance[valve].items():
            if target not in visited:
                new_time_remaining = time_remaining - cost
                if new_time_remaining > 1:
                    stack.append((new_time_remaining, target, released, visited.copy()))

    return results

print('one:', max(allPaths(30).values()))

########################### TWO

# adopted from juanplopes genius idea:
# - calculate all possible one-player paths (including incomplete paths!) that fit in 26 minutes
# - look for combinations of paths that do not both try to open the same valves, take the max

possible_paths = allPaths(26)

max_released = 0
for path1, released1 in possible_paths.items():
    path1 = set(path1)
    path1.remove('AA')
    for path2, released2 in possible_paths.items():
        if path1.isdisjoint(path2):
            max_released = max(max_released, released1+released2)

print('two:', max_released)
