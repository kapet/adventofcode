data = [l.strip() for l in open("2025/01/test.txt")]
tests = [
    (6, data),
    (10, ["R1000"]),
    (2, ["L50", "R100"]),
    (3, ["L50", "L200"]),
    (3, ["R50", "L1", "R1", "R1", "L1"]),
    (4, ["R150", "R200"]),
    (4, ["L150", "L200"]),
]

if 1:
    tests = [(-1, [l.strip() for l in open("2025/01/input.txt")])]


for expected_two, data in tests:
    pos = 50
    one = 0
    two = 0
    for l in data:
        prev = pos
        op = l[0]
        n = int(l[1:])
        assert op in "LR"
        assert 0 < n <= 1000
        if op == "R":
            pos += n
        else:
            pos -= n
        if pos % 100 == 0:
            one += 1
        dist = abs(pos // 100 - prev // 100)
        if op == "L" and prev % 100 == 0:
            dist -= 1
        if op == "R" and pos % 100 == 0:
            dist -= 1
        two += dist
        if pos % 100 == 0:
            two += 1
        #print(f"{l}: {prev} -> {pos} ==> dist={dist} one={one} two={two}")
    print("one", one)
    print("two", two)
    if expected_two >=0 and expected_two != two:
        print("------------ ERROR ------------")
