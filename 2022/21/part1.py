
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
monkeys = dict()
op_chars = ['+', '-', '/', '*']
for line in lines:
    name, instr = line.split(': ')
    is_op = any([x in instr for x in op_chars])
    if is_op:
        monkeys[name] = instr.split(' ')
    else:
        monkeys[name] = int(instr)

def calc(name):
    if isinstance(monkeys[name], int):
        return monkeys[name]
    else:
        a, op, b = monkeys[name]
        a = int(calc(a))
        b = int(calc(b))
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        
print(calc('root'))