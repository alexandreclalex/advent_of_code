
with open('input.txt', 'r') as f:
    lines = [line for line in f]
    
instructions = [line.split() for line in lines]
for instruction in instructions:
    if len(instruction) == 2:
        instruction[1] = int(instruction[1])
        
buffer = [1]

current_instr = 0
while current_instr < len(instructions):
    if len(instructions[current_instr]) == 1:
        buffer.append(buffer[-1])
        current_instr += 1
    else:
        buffer.append(buffer[-1])
        buffer.append(buffer[-1] + instructions[current_instr][1])
        current_instr += 1

total = 0
for i in [20, 60, 100, 140, 180, 220]:
    total += buffer[i-1] * i

print(total)