import copy

input_ = open('input.txt').readlines()
mid = input_.index('\n')

number_of_stacks = len(input_[mid-1].strip().split())
stacks = [[] for _ in range(number_of_stacks)]
for line in input_[0:mid-1]:
    for stack in range(number_of_stacks):
        crate = line[1 + stack*4]
        if crate != ' ':
            stacks[stack].insert(0, crate)

stacks_one = copy.deepcopy(stacks)
stacks_two = stacks
for line in input_[mid+1:]:
    move_n, move_from, move_to = [int(x) for x in line.strip().split()[1:6:2]]
    move_from -= 1
    move_to -= 1

    # task one: crates move one by one
    for _ in range(move_n):
        crate = stacks_one[move_from].pop()
        stacks_one[move_to].append(crate)

    # task two: crates move together
    crates = stacks_two[move_from][0-move_n:]
    del stacks_two[move_from][0-move_n:]
    stacks_two[move_to].extend(crates)

print('one:', ''.join(stacks_one[i][-1] for i in range(number_of_stacks)))
print('two:', ''.join(stacks_two[i][-1] for i in range(number_of_stacks)))
