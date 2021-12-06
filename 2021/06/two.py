import collections

data = [int(i) for i in open('2021/06/input.txt').readline().split(',')]

# no need to hold the full dataset in memory because all 0 behave the same in one round,
# as do all the 1 and so on. We only need how many of each number we have in the set, so
# count it.
data = collections.Counter(data)

print('Initial state: {} fish: {}'.format(sum(data.values()), data))
for iteration in range(1, 257):
    # remember how many 0 we have
    new = data[0]
    # now decrement counters for all fish, just move to lower bucket
    for i in range(8):
        data[i] = data[i+1]
    # those that were in 0 now restart at 6 and spawn an 8
    data[6] += new
    data[8] = new

    if iteration in (18, 80, 256):
        print('After {} days {} fish: {}'.format(iteration, sum(data.values()), data))