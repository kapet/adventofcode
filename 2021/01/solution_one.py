# small enough to load into memory
values = [int(x) for x in open("01/input.txt")]

previous = values[0]
increased = 0
for value in values[1:]:
    if value > previous:
        increased += 1
    previous = value
print(increased)