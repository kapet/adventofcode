valid = 0
for i in range(165432, 707912+1):
    s = str(i)
    found_double = False
    for n in range(1, 6):
        if s[n] < s[n-1]:
            break
        if s[n] == s[n-1]:
            found_double = True
    else:
        if found_double:
            valid += 1
print('one', valid)

valid = 0
for i in range(165432, 707912+1):
    s = str(i)
    found_double = False
    for n in range(1, 6):
        if s[n] < s[n-1]:
            break
        if s[n] == s[n-1]:
            if n>1 and s[n-1] == s[n-2]:
                # same char preceeds
                pass
            elif n<5 and s[n] == s[n+1]:
                # same char follows
                pass
            else:
                found_double = True
    else:
        if found_double:
            valid += 1
print('two', valid)
