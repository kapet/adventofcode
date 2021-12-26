import heapq

import lib

#        0123456ABCDabcdABCDabcd
#start = '.......BCBDDCBADBACADCA'  # test
start = '.......DACDDCBADBACBCBA'  # input
stepcost = {'A':1, 'B':10, 'C':100, 'D':1000}

goal =  '.......ABCDABCDABCDABCD'
goal_positions = {'A': (7, 11, 15, 19), 'B': (8, 12, 16, 20),
                  'C': (9, 13, 17, 21), 'D': (10, 14, 18, 22)}

# only legal positions allowed in this dict
# for every position we store the cheapest cost found to get there and what position from
# [position: key] => (cost: int, prev_position: key)
positional_cost = {start: (0, None)}

# these positions need to be evaluated for followups
# this is a heap managed by heapq module to evaluate the cheapest steps first
# list of (cost: int, position: key)
stack = []
heapq.heappush(stack, (0, start))

while stack:
    cost, position = heapq.heappop(stack)
    assert len(position) == 23
    if positional_cost[position][0] < cost:
        # already know a cheaper path to this position since it was filed,
        # which will have been evaluated already, so can ignore it now
        continue
    if position == goal:
        print('found a solution at cost {}'.format(cost))
        continue

    todo = []
    room_ok = {}

    # check every room for what amphipods are there
    # expect all rooms always fill up from the bottom
    for room in 'ABCD':
        mixed_occupation = False
        room_todo = []
        for i in reversed(goal_positions[room]):
            if position[i] == '.':
                # ignore empty spots, they should be at the top
                continue
            if position[i] != room:
                # if any other type of amphipod is here, this room needs work
                mixed_occupation = True
            if mixed_occupation:
                # if this room needs work, add all amphipods to a list so I can pick the top one next
                room_todo.append(i)
        # mixed_occupation is true if the room is not exclusively the correct amphipod
        # todo contains the top amphipod position, no point moving the others
        # the todo amphipod definitely needs to move out, it is in the way
        if room_todo:
            todo.append(room_todo[-1])
        room_ok[room] = not mixed_occupation

    # check every position in the hallway row for an amphipod
    for i in range(7):
        # if no amphipod, nothing to do
        if position[i] == '.':
            continue

        # amphipods in the hallway can only move if their target room does not have other amphipods
        if room_ok[position[i]]:
            todo.append(i)

    # now we know which amphipods can move at all
    for i in todo:
        destinations = []

        # where should this amphipod ultimately move?
        # they may always move directly to the target room if it has no other amphipods
        if room_ok[position[i]]:
            for j in reversed(goal_positions[position[i]]):
                if position[j] == '.':
                    destinations.append(j)
                    break
        
        if i>6:
            # this amphipod is in a room, so it may move into the hallway
            destinations.extend(range(7))

        # hallway amphipods may only move directly into the correct destination
        for j in destinations:
            if position[j] == '.' and lib.check_path(position, i, j):
                # found an empty, reachable spot - schedule for eval!
                newposition = lib.move(position, i, j)
                newcost = cost + lib.steps(i, j) * stepcost[position[i]]
                if newposition in positional_cost and newcost >= positional_cost[newposition][0]:
                    # know a cheaper path for this position already, ignore it
                    pass
                else:
                    # either don't know this position yet or found a cheaper path
                    # remember and file for eval
                    positional_cost[newposition] = (newcost, position)
                    heapq.heappush(stack, (newcost, newposition))
