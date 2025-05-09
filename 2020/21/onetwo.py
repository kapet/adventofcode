foods = []
for line in open('2020/21/input.txt'):
    ingredients, contains = line.strip().split('(')
    ingredients = ingredients.split()
    contains = contains.rstrip(')').removeprefix('contains ').replace(',', '').split()
    foods.append((ingredients, contains))

# There is a 1:1 mapping between ingredients and allergens.
# If an allergen is listed, then one of the ingredients must have it.
#   The opposite is not true, allergens might be missing from the input.

# Build an index of all ingredients and allergens to nr of food
all_ingredients = {}
all_allergens = {}
for i, (ingredients, contains) in enumerate(foods):
    for ingredient in ingredients:
        all_ingredients.setdefault(ingredient, []).append(i)
    for allergen in contains:
        all_allergens.setdefault(allergen, []).append(i)

# Initially any allergen is possible for any ingredient.
allergens_for_ingredient = {}
for ingredient in all_ingredients.keys():
    allergens_for_ingredient[ingredient] = set(all_allergens.keys())

# Go through all foods and mark unspecified ingredients as not possible for
# the specified allergens.
for ingredients, allergens in foods:
    for other_ingredient in all_ingredients.keys():
        if other_ingredient not in ingredients:
            allergens_for_ingredient[other_ingredient] -= set(allergens)

# Find all ingredients that have already been dropped from any allergen
one = 0
for ingredient, possible_allergens in allergens_for_ingredient.items():
    if len(possible_allergens) == 0:
        one += len(all_ingredients[ingredient])
print('one', one)

# Look for 1:1 mappings between ingredients and allergens and drop these
# ingredients from all other allergens. Keep going until none remain.
keep_going = True
found = []
while keep_going:
    keep_going = False
    for ingredient, possible_allergens in allergens_for_ingredient.items():
        if len(possible_allergens) == 1:
            allergen = possible_allergens.pop()
            found.append((ingredient, allergen))
            keep_going = True
            for other_ingredient in all_ingredients.keys():
                allergens_for_ingredient[other_ingredient].discard(allergen)

found.sort(key=lambda t: t[1])
print('two', ','.join(t[0] for t in found))