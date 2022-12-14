import functools

input_ = open('input.txt')
packets = []
while True:
    left = eval(next(input_))
    right = eval(next(input_))
    packets.append((left, right))
    try:
        next(input_)
    except StopIteration:
        break

def checkOrder(left, right, depth=0):
    # args: left and right are lists
    # returns: -1=wrong order, 1=right order, 0=inconclusive
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            # both are integers, can directly compare!
            if l == r:
                # inconclusive, continue checking
                continue
            else:
                return l < r and 1 or -1

        # at least one is a list, so first make sure both are lists
        if isinstance(l, int):
            l = [l]
        if isinstance(r, int):
            r = [r]

        # now both are lists, compare them
        t = checkOrder(l, r, depth+1)
        if t:
            # sublists were conclusive, break out
            return t

    # comparing the lists was inconclusive, check their lengths!
    if len(left) == len(right):
        # still inconclusive
        return 0
    else:
        return len(left) < len(right) and 1 or -1

correct = 0
for i, (left, right) in enumerate(packets):
    if checkOrder(left, right) == 1:
        correct += i+1
print('one:', correct)

# unpack [(1,2), (3,4)] -> [1,2,3,4]
packets = [p for t in packets for p in t]

div1 = [[2]]
div2 = [[6]]
packets.append(div1)
packets.append(div2)
packets.sort(key=functools.cmp_to_key(checkOrder), reverse=True)
print('two:', (packets.index(div1)+1) * (packets.index(div2)+1))
