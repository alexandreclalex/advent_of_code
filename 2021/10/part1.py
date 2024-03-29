

with open('input.txt') as f:
    lines = [line[:-1] for line in f]

chars = '({[<>]})'
openers = set(chars[:4])
closers = set(chars[4:])

counterparts = dict()
for i in range(8):
    counterparts[chars[i]] = chars[-i-1] 
    
def check_line(line):
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            expected_closer = counterparts[stack.pop()]
            if char != expected_closer:
                # print('Expected', expected_closer, 'but got', char)
                return score_values[char]
    return 0

score_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

print(sum(map(check_line, lines)))
