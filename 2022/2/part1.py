
with open('input.txt') as f:
    moves = [[token for token in line.split()] for line in f]

win_play = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draws = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

total = 0
for opp, play in moves:
    if play == win_play[opp]:
        total += 6
    elif play == draws[opp]:
        total += 3
    total += shape_score[play]

print(total)