test   = 389125467
input_ = 712643589
data = input_

# organization is always clockwise
# very many removals and injections, working with lists very expensive
# use a fixed size array instead, every field points to the next value
# basically a singly-linked list with the pointers stored in an array
# e.g. cups[1]=3 means "after the value 1 comes the value 3"
# wrapped around at the end
# e.g. 1,2,4,3 -> [0, 2, 4, 1, 3]   (not using index 0)
#    1,2,3,4,5 -> [0, 2, 3, 4, 5, 1]

def build(length):
    cups = [None] + list(range(2, length + 1)) + [None]
    values = list(map(int, str(data)))
    for val, nextval in zip(values, values[1:]):
        cups[val] = nextval
    if len(values) == length:
        cups[values[-1]] = values[0]
    else:
        cups[values[-1]] = len(values) + 1
        cups[-1] = values[0]
    return values[0], cups

def play(current, cups, moves):
    for move in range(moves):
        pickup_first = cups[current]
        pickup_second = cups[pickup_first]
        pickup_last = cups[pickup_second]

        # remove the picked up cups, short-cutting from current to after
        cups[current] = cups[pickup_last]

        # find the destination
        destination = current - 1
        while True:
            if destination <= 0:
                destination = len(cups)-1
            if destination in (pickup_first, pickup_second, pickup_last):
                destination -= 1
            else:
                break

        # now insert the picked up items after the destination
        tmp = cups[destination]
        cups[destination] = pickup_first
        cups[pickup_last] = tmp

        current = cups[current]
    return cups


current, cups = build(9)
cups = play(current, cups, 100)
one = []
current = 1
while len(one) < 8:
    current = cups[current]
    one.append(str(current))
print('one', ''.join(one))

current, cups = build(1_000_000)
cups = play(current, cups, 10_000_000)
print('two', cups[1] * cups[cups[1]])
