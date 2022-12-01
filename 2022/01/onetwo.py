elves = []
elf = 0
for line in open('input.txt'):
  try:
    elf += int(line)
  except ValueError:
    elves.append(elf)
    elf = 0
if elf:
  elves.append(elf)

elves.sort()
print('one', elves[-1])
print('two', sum(elves[-3:]))
