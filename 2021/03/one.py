import collections

freq = collections.defaultdict(collections.Counter)
for line in open('2021/03/input.txt'):
    line = line.strip()
    for i in range(len(line)):
        freq[i][line[i]] += 1

print(freq)

gamma = ''
epsilon = ''
for position in sorted(freq.keys()):
    by_frequency = freq[position].most_common()
    gamma += by_frequency[0][0]
    epsilon += by_frequency[1][0]

print(gamma, epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma, epsilon, gamma*epsilon)