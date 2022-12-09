def tuple_add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def tuple_sub(t1, t2):
    return (t1[0]-t2[0], t1[1]-t2[1])

def sign(value):
    return value >= 0 and 1 or -1

def move_tail(parent, pos):
    diff = tuple_sub(parent, pos)
    tail_step = (0, 0)
    if diff[0] == 0:
        # head and tail on same x coordinate
        if abs(diff[1]) > 1:
            tail_step = (0, sign(diff[1]))
    elif diff[1] == 0:
        # head and tail on same y coordinate
        if abs(diff[0]) > 1:
            tail_step = (sign(diff[0]), 0)
    elif abs(diff[0])+abs(diff[1]) > 2:
        # diagonally don't touch
        tail_step = (sign(diff[0]), sign(diff[1]))
    return tuple_add(pos, tail_step)

# x and y like in a normal coordinate system
vectors = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

# ONE
pos_head = (0, 0) # (x,y)
pos_tail = pos_head
all_tail_positions = set()

# TWO
snake = [(0,0)] * 10
all_snake_tail_positions = set()

for line in open('input.txt'):
    direction, distance = line.strip().split()

    for i in range(int(distance)):
        # ONE
        pos_head = tuple_add(pos_head, vectors[direction])
        pos_tail = move_tail(pos_head, pos_tail)
        all_tail_positions.add(pos_tail)

        # TWO
        snake[0] = tuple_add(snake[0], vectors[direction])
        for i in range(1, 10):
            snake[i] = move_tail(snake[i-1], snake[i])
        all_snake_tail_positions.add(snake[-1])

print('one:', len(all_tail_positions))
print('two:', len(all_snake_tail_positions))
