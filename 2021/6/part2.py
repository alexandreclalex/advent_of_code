DESIRED_DAYS = 256

with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().split(',')))
    
counts = [0]*9
for value in arr:
    counts[value] += 1

def do_day(fish_counts):
    zero_count = fish_counts[0]
    new_counts = fish_counts[1:] + [0]
    new_counts[8] += zero_count
    new_counts[6] += zero_count
    return new_counts


days = [counts]

while len(days) <= DESIRED_DAYS:
    days.append(do_day(days[-1]))

print(sum(days[-1]))