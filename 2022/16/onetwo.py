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
#   30 min left (plus 1 min to 'open' the valve in AA)
#   on node AA
#   0 pressure released
#   no nodes visited yet
stack = [(31, 'AA', 0, set())]
max_released = 0
while stack:
    time_remaining, valve, released, visited = stack.pop(0)
    visited.add(valve)

    # open this valve, calculate pressure release for remaining time
    time_remaining -= 1
    released += time_remaining * flowrate[valve]

    # move on to nodes that can be reached within available time
    moving_on = False
    for target,cost in distance[valve].items():
        if target not in visited:
            new_time_remaining = time_remaining - cost
            if new_time_remaining > 1:
                stack.append((new_time_remaining, target, released, visited.copy()))
                moving_on = True

    if not moving_on:
        max_released = max(max_released, released)

print('one:', max_released)

########################### TWO

visited_optimum = {} # visited set -> best release

# start iteration:
#   26 min left (plus 1 min to 'open' the valve in AA)
#   both on node AA with no remaining waiting time
#   0 pressure released
#   no nodes visited yet
stack = [(26+1, ('AA', 0), ('AA', 0), 0, set([]))]
max_released = 0
last_min = 0
while stack:
    time_remaining, p1, p2, released, visited = stack.pop(0)
    p1_valve, p1_wait = p1
    p2_valve, p2_wait = p2

    if time_remaining != last_min:
        print('   ', time_remaining, len(stack), len(visited_optimum))
        last_min = time_remaining

    time_remaining -= 1

    if p1_wait == 0:
        visited.add(p1_valve)
        released += time_remaining * flowrate[p1_valve]
        p1_next = []
        for target, cost in distance[p1_valve].items():
            if target != p2_valve and target not in visited and time_remaining - cost > 1:
                p1_next.append((target, cost))
        if not p1_next:
            p1_next.append(('$$', 999))
    else:
        p1_next = [(p1_valve, p1_wait-1)]

    if p2_wait == 0:
        visited.add(p2_valve)
        released += time_remaining * flowrate[p2_valve]
        p2_next = []
        for target, cost in distance[p2_valve].items():
             if target != p1_valve and target not in visited and time_remaining - cost > 1:
                p2_next.append((target, cost))
        if not p2_next:
            p2_next.append(('$$', 999))
    else:
        p2_next = [(p2_valve, p2_wait-1)]

    visited_key = tuple(sorted(visited))
    if released < visited_optimum.get(visited_key, 0):
        # there's another path that achieved bigger release with the same set of nodes visited
        # drop this path
        continue
    visited_optimum[visited_key] = released

    for p1, p2 in itertools.product(p1_next, p2_next):
        if p1[0] == p2[0]:
            if p1[0] == '$$':
                # done
                if released > max_released:
                    print('new max:', visited, released)
                max_released = max(max_released, released)
                continue
            else:
                # no sense for both players going to the same destination if we're not finished
                # risk: what if only one node remains and BOTH just finished a node?
                continue

        stack.append((time_remaining, p1, p2, released, visited.copy()))

print('two:', max_released)
