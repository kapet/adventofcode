ll = open("2025/12/input.txt").read().split("\n\n")
shapes = []
for ls in ll[:-1]:
    ls = ls.split("\n")[1:]
    assert len(ls) == 3
    assert all(len(s)==3 for s in ls)
    shapes.append(ls)
assert len(shapes) == 6
areas = []
for la in ll[-1].split("\n"):
    size, numbers = la.split(": ")
    size = [int(i) for i in size.split("x")]
    numbers = [int(i) for i in numbers.split()]
    assert len(size) == 2
    assert len(numbers) == 6
    areas.append((size, numbers))

weight = [sum(sum(x=='#' for x in l) for l in ll) for ll in shapes]
too_much = no_problem = 0
for a in areas:
    space = a[0][0]*a[0][1]
    total_weight = sum(weight[i]*a[1][i] for i in range(6))
    if total_weight > space:
        # these can not fit, there is more occupied space than available space
        too_much += 1
    fields = (a[0][0]//3)*(a[0][1]//3)
    presents = sum(a[1])
    if fields >= presents:
        # these can fit without any overlap
        no_problem += 1
if too_much + no_problem == len(areas):
    print("one", no_problem)
else:
    raise Exception("OMG")
