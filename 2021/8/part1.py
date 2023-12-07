
lines = []

with open('input.txt', 'r') as f:
    for line in f:
        tokens = line.split()
        lines.append((tokens[:10], tokens[11:]))
        
len_1478 = set([2, 4, 3, 7])

count = 0
for signal, output in lines:
    for value in output:
        if len(value) in len_1478:
            count += 1

print(count)