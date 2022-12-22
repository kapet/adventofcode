def mix(order, data, output=False):
    if output:
        print('original:')
        print('  ', [t[1] for t in data])

    for element in order:
        if element[1] == 0:
            continue

        # find element and remove from array
        i = data.index(element)
        _, n = data.pop(i)

        # calculate new position of element
        # wrap negative numbers around to positive
        # handle off-by-one due to keeping jumped-over elements in place
        j = (i + n + len(data) - 1) % len(data) + 1

        if output:
            print('{} at {} (of {}) -> {}'.format(n, i, len(data), j))

        data.insert(j, element)

        if output:
            print('  ', [t[1] for t in data])

# there are duplicate values in the input set! *gnarg*
data = []
zero = None
for i, line in enumerate(open('2022/20/input.txt')):
    element = (i, int(line.strip()))
    data.append(element)
    if element[1] == 0:
        zero = element

original = data[:]
mix(original, data)
i = data.index(zero)
print('one:', data[(i + 1000) % len(data)][1] + data[(i + 2000) % len(data)][1] + data[(i + 3000) % len(data)][1])

original = [(i, n*811589153) for i,n in original]
data = original[:]
for _ in range(10):
    mix(original, data)
i = data.index(zero)
print('two:', data[(i + 1000) % len(data)][1] + data[(i + 2000) % len(data)][1] + data[(i + 3000) % len(data)][1])
