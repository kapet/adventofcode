passports = []
p = {}
for l in open('2020/04/input.txt'):
    l = l.split()
    if not l:
        passports.append(p)
        p = {}
    else:
        for ll in l:
            k, v = ll.split(':')
            p[k] = v
passports.append(p)

one = two = 0
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
for p in passports:
    if required.issubset(set(p.keys())):
        one += 1

        if not (    1920 <= int(p['byr']) <= 2002
                and 2010 <= int(p['iyr']) <= 2020
                and 2020 <= int(p['eyr']) <= 2030):
            continue
        if p['hgt'].endswith('cm') and 150 <= int(p['hgt'][:-2]) <= 193:
            pass
        elif p['hgt'].endswith('in') and 59 <= int(p['hgt'][:-2]) <= 76:
            pass
        else:
            continue
        if len(p['hcl'])!=7 or p['hcl'][0]!='#' or any(c not in '0123456789abcdef' for c in p['hcl'][1:]):
            continue
        if p['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if len(p['pid'])!=9 or any(c not in '0123456789' for c in p['pid']):
            continue
        two += 1

print('one', one)
print('two', two)
