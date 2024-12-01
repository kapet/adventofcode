import collections

data = [map(int, l.split()) for l in open('2024/01/input.txt').readlines()]

# repack columns into sorted lists
list1, list2 = map(sorted, zip(*data))

counter2 = collections.Counter(list2)

sumdist = score = 0
for i in range(len(list1)):
    sumdist += abs(list1[i] - list2[i])
    score += list1[i] * counter2[list1[i]]
print("one:", sumdist)
print("two:", score)
