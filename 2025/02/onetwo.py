import functools

data = [t.strip().split('-') for t in open('2025/02/input.txt').read().split(',')]

@functools.cache
def teiler(n):
    result = [(1, n)]
    if n > 3:
        for i in range(2, n//2+1):
            if n % i == 0:
                result.append((i, n//i))
    result.reverse() # make sure (x,2) is always last
    return result

one = 0
two = 0
for first, last in data:
    for i in range(int(first), int(last)+1):
        if i < 11:
            continue
        txt = str(i)
        for n, m in teiler(len(txt)):
            if (txt[:n] * m) == txt:
                two += i
                if m == 2:
                    one += i
                break
print("one:", one)
print("two:", two)
