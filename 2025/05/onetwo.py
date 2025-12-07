data = open("2025/05/input.txt").readlines()
t = data.index("\n")
fresh = [tuple(int(i) for i in l.split("-")) for l in data[:t]]
available = [int(l) for l in data[t+1:]]

one = 0
for i in available:
    for start, end in fresh:
        if start <= i <= end:
            one += 1
            break
print("one", one)

fresh.sort(key=lambda x:x[0])
result = [list(fresh[0])]
for start, end in fresh[1:]:
    cstart, cend = result[-1]
    if start <= cend+1:
        # extend current range
        result[-1][1] = max(cend, end)
    else:
        # new range
        result.append([start, end])
two = 0
for start, end in result:
    two += (end - start) + 1
print("two", two)
