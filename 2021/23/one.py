import heapq
import time

import lib

#        0123456789abcde
#start = '.......BCBDADCA'  # test
start = '.......DACDBCBA'  # input
stepcost = {'A':1, 'B':10, 'C':100, 'D':1000}

goal =  '.......ABCDABCD'
goal_positions = {'A': (7, 11), 'B': (8, 12), 'C': (9, 13), 'D': (10, 14)}

# only legal positions allowed in this dict
# for every position we store the cheapest cost found to get there and what position from
# [position: key] => (cost: int, prev_position: key)
positional_cost = {start: (0, None)}

# these positions need to be evaluated for followups
# this is a heap managed by heapq module!
# list of (cost: int, position: key)
stack = []
heapq.heappush(stack, (0, start))

t = 0
while stack:
    tn = time.time()
    if tn-t > 1:
        t = tn
        print('evaluated {} positions, {} on stack'.format(len(positional_cost), len(stack)))

    cost, position = heapq.heappop(stack)
    assert len(position) == 15
    if positional_cost[position][0] < cost:
        # already know a cheaper path to this position since it was filed,
        # which will have been evaluated already, so can ignore it now
        continue
    if position == goal:
        print('found a solution at cost {}'.format(cost))
        continue

    # check every position in the hallway row for an amphipod
    for i in range(7):
        # if no amphipod, nothing to do
        if position[i] == '.':
            continue

        # where should this amphipod ultimately move?
        goals = goal_positions[position[i]]

        # hallway amphipods may only move directly into the correct destination
        for j in goals:
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

    # check every position in the rooms for an amphipod
    for i in range(7,15):
        # if no amphipod, nothing to do
        if position[i] == '.':
            continue

        # where should this amphipod ultimately move?
        goals = goal_positions[position[i]]

        # room amphipods can move into the hallway or straight into the correct destination

        # check if at destination, or if can move there
        if i in goals and i in (0xb, 0xc, 0xd, 0xe):
            # amphipod is in the right room already!
            # is in the back position and not blocking anything, leave here
            pass
        elif i in goals and position[i+4] == position[i]:
            # amphipod is in the right room already!
            # the other position is occupied by the right one too, leave here
            pass
        else:
            # amphipod is in the wrong room or is blocking another amphipod
            # try moving into the hallway or into the right room
            for j in list(range(7))+list(goals):
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
