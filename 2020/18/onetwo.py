import math

formulas = [l.strip().replace(" ", "") for l in open('2020/18/input.txt')]

class Parser:
    def __init__(self, f, advanced=False):
        self.f = f
        self.i = 0
        self.advanced = advanced

    def lookahead(self):
        if self.i < len(self.f):
            return self.f[self.i]
        else:
            return None

    def read(self):
        c = self.lookahead()
        self.i += 1
        return c
    
    def expect(self, c):
        assert c == self.read()
    
    def term(self):
        if self.lookahead() == '(':
            self.expect('(')
            result = self.expression()
            self.expect(')')
        else:
            result = int(self.read())
        return result
    
    def expression(self):
        mults = []
        value = self.term()
        while self.lookahead() in ['+', '*']:
            if self.read() == '+':
                value += self.term()
            else:
                if self.advanced:
                    mults.append(value)
                    value = self.term()
                else:
                    value *= self.term()
        return value * math.prod(mults)
    
    def result(self):
        val = self.expression()
        assert self.i == len(self.f)
        return val


one = 0
two = 0
for f in formulas:
    p = Parser(f)
    one += p.result()

    p.i = 0
    p.advanced = True
    two += p.result()

print('one', one)
print('two', two)