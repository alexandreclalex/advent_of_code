

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
            expected_closer = counterparts[stack.pop]
            if char != counterparts[expected_closer]:
                return expected_closer
    return None

score_values = {
    ')': 3,
    ']': 57,
    
}

score = 0
