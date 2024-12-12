import functools

test = [125, 17]
input = list(map(int, open('2024/11/input.txt').read().split()))
stones = input

@functools.cache
def step(stone):
    if stone == 0:
        return (1,)

    s = str(stone)
    n = len(s)
    d,m = divmod(n, 2)
    if m == 0:
        return (int(s[:d]), int(s[d:]))

    return (stone * 2024,)

@functools.cache
def width(stone, blinks):
    if blinks == 0:
        return 1
    
    return sum(width(s, blinks-1) for s in step(stone))

one = sum(width(s, 25) for s in stones)
print('one', one)

two = sum(width(s, 75) for s in stones)
print('two', two)
