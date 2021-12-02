# small enough to load into memory
values = [int(x) for x in open("2021/01/input.txt")]

previous = sum(values[0:3])
increased = 0
for i in range(1, len(values)-2):
    # sliding window sum of 3 is fast, no point in complex subtract/add code
    value = sum(values[i:i+3])
    if value > previous:
        increased += 1
    previous = value
print(increased)