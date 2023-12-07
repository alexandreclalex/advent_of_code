import itertools
from more_itertools import bucket, one

lines = []
    
with open('input.txt', 'r') as f:
    for line in f:
        tokens = line.split()
        lines.append((tokens[:10], tokens[11:]))
        
display_segments = [
    set('abcedf'), 
    set('cf'),
    set('acdeg'),
    set('acdfg'),
    set('bcdf'),
    set('abdfg'),
    set('abdefg'),
    set('acf'),
    set('abcdefg'),
    set('abcdfg')
    ]

segment_counts = {
    2:[1],
    3:[7],
    4:[4],
    5:[2, 3, 5],
    6:[0, 6, 9],
    7:[8]
    }

def generate_mapping(signal_set):
    key_sets = [None for _ in range(10)]
    segment_mapping = {i: set('abcdef') for i in 'abcdefg'}
    unknown_signals = []
    for signal in signal_set:
        if len(segment_counts[len(signal)]) == 1:
            # Only one possible value for this key
            signal_value = segment_counts[len(signal)][0]
            key_sets[signal_value] = set(signal)
            for segment in signal:
                # Deletes all segment possibilities that do not make up the known number
                segment_mapping[segment] = segment_mapping[segment].intersection(display_segments[signal_value])
        else:
            unknown_signals.append(set(signal))
            
    
    print(segment_mapping)
    
def calc_line(line):
    signal_patterns, output_values = line[0], line[1]

    patterns = itertools.chain(signal_patterns, output_values)

    groups = bucket(patterns, key=len)
    patterns_by_length = {length: {"".join(sorted(pattern)) for pattern in groups[length]} for length in groups}

    one_pattern = one(patterns_by_length[2])  # 1 is the only digit that uses 2 segments
    four_pattern = one(patterns_by_length[4])  # 4 is the only digit that uses 4 segments
    seven_pattern = one(patterns_by_length[3])  # 7 is the only digit that uses 3 segments

    pattern_to_digit = {"abcdefg": 8, one_pattern: 1, four_pattern: 4, seven_pattern: 7}

    one_segments = set(one_pattern)
    four_segments = set(four_pattern)

    # 3 is the only digit that uses 5 segments and both of the segments on the right (the segments in 1)
    three_pattern = one(p for p in patterns_by_length[5] if all(x in p for x in one_segments))
    pattern_to_digit[three_pattern] = 3

    # 6 is the only digit that uses 6 segments and only one of the segments in digit 1
    six_pattern = one(p for p in patterns_by_length[6] if sum(x in p for x in one_segments) == 1)
    pattern_to_digit[six_pattern] = 6

    # 2 is the only digit that uses 5 segments and has 2 segments in common w/ 4
    two_pattern = one(p for p in patterns_by_length[5] if sum(x in p for x in four_segments) == 2)
    pattern_to_digit[two_pattern] = 2

    # 5 is the only remaining digit that uses 5 segments
    five_pattern = one(p for p in patterns_by_length[5] if p not in (two_pattern, three_pattern))
    pattern_to_digit[five_pattern] = 5

    # 9 is the only digit that uses 6 segments and has 4 segments in common w/ 4
    nine_pattern = one(p for p in patterns_by_length[6] if sum(x in p for x in four_segments) == 4)
    pattern_to_digit[nine_pattern] = 9

    # 0 is the only remaining digit that uses 6 segmensts
    zero_pattern = one(p for p in patterns_by_length[6] if p not in (six_pattern, nine_pattern))
    pattern_to_digit[zero_pattern] = 0

    output_digits = [pattern_to_digit["".join(sorted(output_value))] for output_value in output_values]
    return sum(10**i * n for i, n in enumerate(reversed(output_digits)))

print(sum(map(calc_line, lines)))