import functools

data = [l.strip() for l in open("2025/03/input.txt")]

@functools.cache
def highest(bank, n):
    rest_n = n - 1
    first = sorted(bank[:len(bank)-rest_n], reverse=True)[0]
    i = bank.index(first)
    if rest_n:
        rest = highest(bank[i+1:], rest_n)
    else:
        rest = ""
    return first + rest

assert highest("1", 1) == "1"
assert highest("123", 1) == "3"
assert highest("12", 2) == "12"
assert highest("123", 2) == "23"
assert highest("213", 2) == "23"
assert highest("231", 2) == "31"
assert highest("123", 3) == "123"

one = two = 0
for bank in data:
    one += int(highest(bank, 2))
    two += int(highest(bank, 12))
print("one:", one)
print("two:", two)
