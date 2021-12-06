data = [int(i) for i in open('2021/06/input.txt').readline().split(',')]

#print('Initial state: {}'.format(','.join(str(d) for d in data)))
for iteration in range(1, 81):
    new = 0
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            new += 1
        else:
            data[i] -= 1
    data.extend([8]*new)

    if iteration in (18, 80):
        print('After {} days {} fish'.format(iteration, len(data)))
    #print('After {} days: {}'.format(iteration, ','.join(str(d) for d in data)))