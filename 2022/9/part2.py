

with open('input.txt', 'r') as f:
    moves = [line.split() for line in f]

for move in moves:
    move[1] = int(move[1])

knots = [[0]*2 for _ in range(10)]

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

def move_tail(head, tail):
    if head[0]!=tail[0] and head[1]!=tail[1] and abs(head[0]-tail[0])+abs(head[1]-tail[1])>2:
        xdist = head[0]-tail[0]
        ydist = head[1]-tail[1]
        tail[0] += xdist // abs(xdist)
        tail[1] += ydist // abs(ydist)
    elif head[0]-tail[0] > 1:
        tail[0] += 1
    elif head[0]-tail[0] < -1:
        tail[0] -= 1
    elif head[1]-tail[1] > 1:
        tail[1] += 1
    elif head[1]-tail[1] < -1:
        tail[1] -= 1
        
positions = set()

for move in moves:
    direction = directions[move[0]]
    for i in range(move[1]):
        for x in range(2):
            knots[0][x] += direction[x]
        for i in range(1, len(knots)):
            move_tail(knots[i-1], knots[i])
        positions.add(tuple(knots[-1]))

print(len(positions))