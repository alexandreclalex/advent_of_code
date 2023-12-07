
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

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

move_index = {
    'X': lose,
    'Y': draws,
    'Z': win_play
}

with open('input.txt') as f:
    raw_moves = [[token for token in line.split()] for line in f]
    
moves = []
for move in raw_moves:
    moves.append((move[0], move_index[move[1]][move[0]]))
    

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