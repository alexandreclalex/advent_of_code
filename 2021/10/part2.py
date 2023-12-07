from statistics import median

with open('input.txt') as f:
    lines = [line[:-1] for line in f]

chars = '({[<>]})'
openers = set(chars[:4])
closers = set(chars[4:])

counterparts = dict()
for i in range(8):
    counterparts[chars[i]] = chars[-i-1] 
    

def score_remaining(stack):
    values = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for val in stack[::-1]:
        score *=5
        score += values[counterparts[val]]
    return score
    
def check_line(line):
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            expected_closer = counterparts[stack.pop()]
            if char != expected_closer:
                return None
    return score_remaining(stack)

score_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores = []
for line in lines:
    score = check_line(line)
    if score is not None:
        scores.append(score)

print(median(scores))