from more_itertools import one

letters = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
def rucksack_type(line):
    half = len(line) // 2
    first = set(line[:half])
    second = set(line[half:])
    return one(first.intersection(second))

print(sum([letters.index(rucksack_type(x)) for x in lines]))