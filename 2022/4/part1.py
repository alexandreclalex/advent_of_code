

with open('input.txt', 'r') as f:
    raw_pairs = [line[:-1].split(',') for line in f]

pairs = []
for pair in raw_pairs:
    pairs.append([list(map(int, x.split('-'))) for x in pair])

counter = 0
for r1, r2 in pairs:
    if (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r1[0] >= r2[0] and r1[1] <= r2[1]):
        counter += 1

print(counter)