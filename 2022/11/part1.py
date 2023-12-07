
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
class Monkey:
    def __init__(self) -> None:
        self.mult = 0
        self.check = 0
        self.op = None
        self.items = []
        self.operation = None
        self.condition = None
        self.true = None
        self.false = None
    
monkeys = []

for i in range(0, len(lines), 7):
    m = Monkey()
    raw_tokens = [token for token in lines[i+1].split()[2:]]
    for j, token in enumerate(raw_tokens):
        if len(token) == 3:
            raw_tokens[j] = token[:-1]
    m.items = [int(token) for token in raw_tokens]
    op_line = lines[i+2].split()
    m.mult = op_line[5]
    m.op = op_line[4]

    m.check = int(lines[i+3].split()[3])
    m.true = int(lines[i+4].split()[5])
    m.false = int(lines[i+5].split()[5])
    monkeys.append(m)
    
inspections = [0]*len(monkeys)
for round in range(20):
    for i, m in enumerate(monkeys):
        for item in m.items:
            if m.mult == 'old':
                new_item = item*item
            elif m.op == '+':
                new_item = item+ int(m.mult)
            elif m.op == '*':
                new_item = item* int(m.mult)
            inspections[i] += 1
            new_item //= 3
            next_monkey = m.true if new_item % m.check == 0 else m.false
            monkeys[next_monkey].items.append(new_item)
        m.items = []

sorted_inspections = sorted(inspections)

print(sorted_inspections[-2] * sorted_inspections[-1])
            