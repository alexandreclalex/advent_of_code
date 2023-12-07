
with open('input.txt', 'r') as f:
    lines = [line for line in f]
    
instructions = [line.split() for line in lines]
for instruction in instructions:
    if len(instruction) == 2:
        instruction[1] = int(instruction[1])
        
buffer = [1]
pos = 1

current_instr = 0
while current_instr < len(instructions):
    if len(instructions[current_instr]) == 1:
        buffer.append(buffer[-1])
        current_instr += 1
    else:
        buffer.append(buffer[-1])
        buffer.append(buffer[-1] + instructions[current_instr][1])
        current_instr += 1

cycle = 0
while cycle < len(buffer):
    xval = buffer[cycle]
    
    if abs(xval - (cycle%40)) < 2:
        print('#', end = '')
    else:
        print('.', end = '')
    
    cycle += 1
    if cycle%40 ==0:
        print()