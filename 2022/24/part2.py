from queue import PriorityQueue

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
board = [list(line[1:-1]) for line in lines[1:-1]]

start = (-1, lines[0].index('.') - 1)
end = (len(lines)-2, lines[-1].index('.') - 1)

deltas = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

blizzards = set()

for i, row in enumerate(board):
    for j, elem in enumerate(row):
        if elem in deltas:
            blizzards.add((i, j, deltas[elem]))

def move(blizzard):
    y, x, delta = blizzard
    dy, dx = delta
    return ((y+dy)%len(board), (x+dx)%len(board[0]), delta)

def step(blizzards):
    return set(map(move, blizzards))

board_states = [blizzards]
def gen_states_until(n):
    while len(board_states) < n+1:
        board_states.append(step(board_states[-1]))
        
def valid_pos(pos, time):
    y, x = pos
    return not any([(y, x, delta) in board_states[time] for delta in deltas.values()])

def score(pos, time):
    return ((pos[0] - end[0])**2 + (pos[0] - end[0])**2) / time

gen_states_until(1000)
directions = list(deltas.values()) + [(0, 0)]

completed_trips = 0
possible = set()
possible.add(start)
for time in range(1, 100000000):
    next_possible = set()
    for prev in possible:
        y, x = prev
        for dy, dx in directions:
            if 0 <= y+dy < len(board) and 0 <= x+dx < len(board[0]) or (y+dy, x+dx) in [start, end]:
                pos = (y+dy, x+dx)
                if valid_pos(pos, time+1):
                    next_possible.add(pos)
    if end in next_possible:
        completed_trips += 1
        print(f'Completed trip {completed_trips} at {time+1}')
        if completed_trips == 3:
            break
        else:
            next_possible = set([end])
            start, end = end, start
    possible = next_possible
