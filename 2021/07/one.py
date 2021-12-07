import collections

data = [int(i) for i in open('2021/07/input.txt').readline().split(',')]

data = collections.Counter(data)
low = min(data)
high = max(data)

lowest = high*len(data)
for i in range(low, high+1):
    cost = sum(cnt*abs(elem-i) for elem, cnt in data.items())
    if cost < lowest:
        lowest = cost
    print('pos {} cost {}'.format(i, cost))

print('lowest was {}'.format(lowest))