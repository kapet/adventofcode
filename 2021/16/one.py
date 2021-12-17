test1 = 'D2FE28' # 2021
test2 = '38006F45291200'
test3 = 'EE00D40C823060'
test4 = '8A004A801A8002F478'
test5 = '620080001611562C8802118E34'
test6 = 'C0015000016115A2E0802F182340'
test7 = 'A0016C880162017C3686B18A3D4780'
testinput = open('2021/16/input.txt').readline().strip()

transmission = testinput

# convert into list of bits
transmission = list(''.join('{:04b}'.format(int(t, 16)) for t in transmission))

def get(bits):
    val = 0
    for _ in range(bits):
        val <<= 1
        if transmission.pop(0) == '1':
            val |= 1
#    print('                                      get({}) => {}'.format(bits, val))
    return val

def packet(tabs):
    version = get(3)
    typeid = get(3)
    print('  '*tabs + 'PACKET v{} t{}'.format(version, typeid))
    tabs += 1

    if typeid == 4:
        # literal value
        value = 0
        while True:
            val = get(5)
            value = (value << 4) | (val & 0x0f)
            if not (val & 0x10):
                break
        print('  '*tabs + 'literal {}'.format(value))

    else:
        # operator
        if get(1) == 0:  # Length Type ID
            # number of bits given
            target_length = 0 - get(15) + len(transmission)  # get modifies transmission!
            while len(transmission) > target_length:
                version += packet(tabs)
        else:
            # number of sub-packets given
            for _ in range(get(11)):
                version += packet(tabs)

    return version

version_sum = packet(0)
print('rest: {}'.format(''.join(transmission)))
print('version sum: {}'.format(version_sum))