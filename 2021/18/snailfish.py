def parse(line):
    result = []
    buffer = ''
    for c in line:
        if c in '[],':
            if buffer:
                result.append(int(buffer))
                buffer = ''
            result.append(c)
        else:
            buffer += c
    return result

def output(num):
    return ''.join(str(t) for t in num)

def add(num1, num2):
    return ['['] + num1[:] + [','] + num2[:] + [']']

def _reduce_explode(num):
    depth = 0
    for i in range(len(num)):
        v = num[i]
        if v == '[':
            depth += 1
            if depth == 5:
                # this pair needs to be exploded, must be a pair of numbers
                assert num[i+2] == ',' and num[i+4] == ']'
                # extract numbers and replace with a 0
                l = num[i+1]
                r = num[i+3]
                num[i:i+5] = [0]
                # find next number left and add exploded number
                for j in range(i-1, -1, -1):
                    if type(num[j]) == int:
                        num[j] += l
                        break
                # same for next number right
                for j in range(i+1, len(num)):
                    if type(num[j]) == int:
                        num[j] += r
                        break
                return True
        elif v == ']':
            depth -= 1
    
    # found nothing to explode
    return False

def _reduce_split(num):
    for i in range(len(num)):
        v = num[i]
        if type(v) is int and v >= 10:
            # split this number
            l = v // 2
            r = v-l
            # replace current number with pair
            num[i:i+1] = ['[', l, ',', r, ']']
            return True

    # found nothing to split
    return False

def reduce(num):
    while True:
        if _reduce_explode(num):
            continue
        if _reduce_split(num):
            continue
        break

def _magnitude(num, ptr):
    if type(num[ptr]) == int:
        # magnitude of a number is the number itself
        return num[ptr], ptr+1
    else:
        # magnitude of a pair based on its left and right values, get them
        l, ptr = _magnitude(num, ptr+1)
        r, ptr = _magnitude(num, ptr+1)
        return 3*l+2*r, ptr+1

def magnitude(num):
    mag, _ = _magnitude(num, 0)
    return mag
