# Only iterate through each string once per task, so complexity not a concern.
# Just cut out the number of chars and convert that substring into a set.
# The length of the set is then the number of different chars.

for line in open('input.txt'):
    print('---')
    line = line.strip()
    for i in range(len(line)-4):
        if len(set(line[i:i+4])) == 4:
            print('one:', i+4)
            break

    for i in range(len(line)-14):
        if len(set(line[i:i+14])) == 14:
            print('two:', i+14)
            break
