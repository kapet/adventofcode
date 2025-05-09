lines = open('2020/13/input.txt').readlines()
timestamp = int(lines[0].strip())
busses = set(int(i) for i in lines[1].split(',') if i!='x')

departures = [(bus, (timestamp // bus + 1) * bus) for bus in busses]
bus, earliest = min(departures, key=lambda x: x[1])
print('one', (earliest-timestamp)*bus)

#lines[1] = '1789,37,47,1889'
goal = []
for i, t in enumerate(lines[1].strip().split(',')):
    if t != 'x':
        goal.append((int(t), i))

# Start by moving forward with the first bus' interval
position = 0
interval = goal[0][0]

for bus, offset in goal[1:-1]:
    # Move forward with the current interval and look for the perfect offset to
    # the next bus.
    while (position+offset) % bus != 0:
        position += interval
    # Found a position where all busses looked at so far have the right offsets.
    pstart = position
    # Now look for the next such position by scanning forward with the current
    # interval again.
    position += interval
    while (position+offset) % bus != 0:
        position += interval
    # Found another position where all busses looked at so far have the right
    # offsets. This means that from here on out every this distance the busses
    # are positioned right again. So take this interval from now on.
    interval = position - pstart

# Just look for the first match for the last bus. This is the final solution.
bus, offset = goal[-1]
while (position+offset) % bus != 0:
    position += interval
print('two', position)
