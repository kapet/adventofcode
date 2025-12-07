def load(filename):
    with open(filename) as infile:
        data = infile.read().strip()
    return list(map(int, data.split(',')))

def _param(mem, pc, pmodes):
    pmodes, pmode = divmod(pmodes, 10)
    if pmode == 0:
        value = mem[mem[pc]]
        debug = f'[{mem[pc]}]'
    elif pmode == 1:
        value = mem[pc]
        debug = f'{mem[pc]}'
    else:
        raise Exception()
    return value, pmodes, debug

def run(mem, input_=[], debug=False):
    output_ = []
    pc = 0
    while True:
        pmodes, opcode = divmod(mem[pc], 100)
        if opcode == 1:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            dest = mem[pc+3]
            mem[dest] = a + b
            if debug:
                print(f'@{pc:04} ADD {_a} + {_b} => [{dest}] // {a}+{b}={a+b}')
            pc += 4
        elif opcode == 2:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            dest = mem[pc+3]
            mem[dest] = a * b
            if debug:
                print(f'@{pc:04} MUL {_a} * {_b} => [{dest}] // {a}*{b}={a*b}')
            pc += 4
        elif opcode == 3:
            dest = mem[pc+1]
            mem[dest] = input_.pop(0)
            if debug:
                print(f'@{pc:04} IN  => [{dest}] // {mem[dest]}')
            pc += 2
        elif opcode == 4:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            output_.append(a)
            if debug:
                print(f'@{pc:04} OUT {_a} // {a}')
            pc += 2
        elif opcode == 5:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            if debug:
                print(f'@{pc:04} IF {_a}!=0 JMP {_b} // {a}? ->{b}')
            if a != 0:
                pc = b
            else:
                pc += 3
        elif opcode == 6:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            if debug:
                print(f'@{pc:04} IF {_a}==0 JMP {_b} // {a}? ->{b}')
            if a == 0:
                pc = b
            else:
                pc += 3
        elif opcode == 7:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            c = mem[pc+3]
            mem[c] = a < b and 1 or 0
            if debug:
                print(f'@{pc:04} IF {_a}<{_b} THEN 1=>[{c}] // {a}<{b}? => {mem[c]}')
            pc += 4
        elif opcode == 8:
            a, pmodes, _a = _param(mem, pc+1, pmodes)
            b, pmodes, _b = _param(mem, pc+2, pmodes)
            c = mem[pc+3]
            mem[c] = a == b and 1 or 0
            if debug:
                print(f'@{pc:04} IF {_a}=={_b} THEN 1=>[{c}] // {a}=={b}? => {mem[c]}')
            pc += 4
        elif opcode == 99:
            if debug:
                print(f'@{pc:04} BRK')
            pc += 1
            break
        else:
            raise Exception()
    return output_
