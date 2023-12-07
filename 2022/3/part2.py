from more_itertools import one

letters = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
def badge(line1, line2, line3):
    sets = [set(x) for x in (line1, line2, line3)]
    return one(sets[0].intersection(sets[1]).intersection(sets[2]))

badges = []
for i in range(0, len(lines), 3):
    badges.append(badge(lines[i], lines[i+1], lines[i+2]))
    
print(sum([letters.index(b) for b in badges]))