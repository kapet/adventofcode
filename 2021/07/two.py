import collections

data = [int(i) for i in open('2021/07/input.txt').readline().split(',')]

data = collections.Counter(data)
low = min(data)
high = max(data)

dist_cost = [0]
cost = 0
for i in range(1, high-low+1):
    cost += i
    dist_cost.append(cost)

lowest = 99999999999999
for i in range(low, high+1):
    cost = sum(cnt*dist_cost[abs(elem-i)] for elem, cnt in data.items())
    if cost < lowest:
        lowest = cost
    print('pos {} cost {}'.format(i, cost))

print('lowest was {}'.format(lowest))