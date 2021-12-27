def ALU(program, input_data):
    input_data = input_data[:]
    registers = {'w':0, 'x':0, 'y':0, 'z':0}
    for line in program:
        if line[0] == 'inp':
            r = line[1]
            registers[r] = input_data.pop(0)
        elif line[0] == 'add':
            r = line[1]
            o = line[2]
            if o in 'wxyz':
                registers[r] += registers[o]
            else:
                registers[r] += int(o)
        elif line[0] == 'mul':
            r = line[1]
            o = line[2]
            if o in 'wxyz':
                registers[r] *= registers[o]
            else:
                registers[r] *= int(o)
        elif line[0] == 'div':
            r = line[1]
            o = line[2]
            if o in 'wxyz':
                registers[r] /= registers[o]
            else:
                registers[r] //= int(o)
        elif line[0] == 'mod':
            r = line[1]
            o = line[2]
            if o in 'wxyz':
                registers[r] %= registers[o]
            else:
                registers[r] %= int(o)
        elif line[0] == 'eql':
            r = line[1]
            o = line[2]
            if o in 'wxyz':
                o = registers[o]
            else:
                o = int(o)
            registers[r] = (registers[r] == o) and 1 or 0
        else:
            raise Exception('unsupported opcode')
    assert len(input_data) == 0
    return registers
