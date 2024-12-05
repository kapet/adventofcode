all_rules = []
all_updates = []

for line in open('2024/05/input.txt'):
    if '|' in line:
        all_rules.append(list(map(int, line.split('|'))))
    elif ',' in line:
        all_updates.append(list(map(int, line.split(','))))

def valid_combinations(pages, rules):
    if not pages:
        return []
    # remove rules not applicable to my set of pages
    rules = [(x,y) for (x,y) in rules if x in pages and y in pages]
    # there will be one page that does not appear as the second page in any rule
    seconds = [y for (_,y) in rules]
    starters = [i for i in pages if i not in seconds]
    assert len(starters) == 1
    # remove this first page, recurse for rest
    return [starters[0]] + valid_combinations(pages^{starters[0]}, rules)

one = two = 0
for update in all_updates:
    c = valid_combinations(set(update), all_rules)
    if c == update:
        one += update[len(update)//2]
    else:
        two += c[len(c)//2]

print('one', one)
print('two', two)
