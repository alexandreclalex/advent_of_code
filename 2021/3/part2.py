lines = []
total_count = 0
with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line[:-1])
        
oxygen_lines = lines.copy()
for i in range(len(oxygen_lines[0])):
    if len(oxygen_lines) == 1:
        break
    count_1 = 0
    for line in oxygen_lines:
        if line[i] == '1':
            count_1 += 1
    most_common = '1' if count_1 >= len(oxygen_lines) / 2 else '0'
    oxygen_lines = [x for x in oxygen_lines if x[i] == most_common]
    
    
co2_lines = lines.copy()
for i in range(len(co2_lines[0])):
    if len(co2_lines) == 1:
        break
    count_1 = 0
    for line in co2_lines:
        if line[i] == '1':
            count_1 += 1
    least_common = '0' if count_1 >= len(co2_lines) / 2 else '1'
    co2_lines = [x for x in co2_lines if x[i] == least_common]

oxygen = int(oxygen_lines[0], 2)
co2 = int(co2_lines[0], 2)

print(oxygen*co2)
