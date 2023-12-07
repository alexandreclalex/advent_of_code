counts = [0]*12
total_count = 0
with open('input.txt', 'r') as f:
    for line in f:
        for i in range(len(line)-1):
            counts[i] += 1 if line[i] == '1' else 0
        total_count += 1

gamma = int("".join(['1' if count > total_count//2 else '0' for count in counts]), 2)
epsilon =  int("".join(['1' if count < total_count//2 else '0' for count in counts]), 2)

print(gamma*epsilon)