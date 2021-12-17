import math

test1 = 'C200B40A82'
test2 = '04005AC33890'
test3 = '880086C3E88112'
test4 = 'CE00C43D881120'
test5 = 'D8005AC2A8F0'
test6 = 'F600BC2D8F'
test7 = '9C005AC2F8F0'
test8 = '9C0141080250320F1802104A08'
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
    value = None

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
        sub_packets = []
        if get(1) == 0:  # Length Type ID
            # number of bits given
            target_length = 0 - get(15) + len(transmission)  # get modifies transmission!
            while len(transmission) > target_length:
                sub_packets.append(packet(tabs))
        else:
            # number of sub-packets given
            for _ in range(get(11)):
                sub_packets.append(packet(tabs))

        if typeid == 0:
            value = sum(sub_packets)
        elif typeid == 1:
            value = math.prod(sub_packets)
        elif typeid == 2:
            value = min(sub_packets)
        elif typeid == 3:
            value = max(sub_packets)
        elif typeid == 5:
            value = sub_packets[0] > sub_packets[1] and 1 or 0
        elif typeid == 6:
            value = sub_packets[0] < sub_packets[1] and 1 or 0
        elif typeid == 7:
            value = sub_packets[0] == sub_packets[1] and 1 or 0

    return value

value = packet(0)
print('rest: {}'.format(''.join(transmission)))
print('value: {}'.format(value))