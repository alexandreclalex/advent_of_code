import re

with open('input.txt', 'r') as f:
    txt = f.read()

boardlines, instr = txt.split('\n\n')

board = boardlines.split('\n')

max_line_len = max([len(line) for line in board])

for i in range(len(board)):
    board[i] += ''.join([' ']*(max_line_len - len(board[i])))

deltas = {
    'L':(-1, 0),
    'R':(1, 0),
    'U':(0, -1),
    'D':(0, 1),
}

directions  = ['R', 'D', 'L', 'U']

instructions = []
num_temp = ''
for char in instr[:-1]:
    if char.isnumeric():
        num_temp += char
    else:
        if num_temp:
            instructions.append(int(num_temp))
            num_temp = ''
        instructions.append(char)
if num_temp:
            instructions.append(int(num_temp))
            num_temp = ''

positions = set()

y = 0
x = board[0].index('.')
facing = 0
for instruction in instructions:
    if isinstance(instruction, str):
        d_facing = 1 if instruction == 'R' else -1
        facing = (facing + d_facing) % len(directions)
        if facing < 0:
            facing += len(directions)
    else:
        dx, dy = deltas[directions[facing]]
        for i in range(instruction):
            n_y = (y+dy) % len(board)
            if n_y < 0:
                n_y += len(board)
            n_x = (x+dx) % len(board[n_y])
            if n_x < 0:
                n_x += len(board[n_y])
                
            while board[n_y][n_x] == ' ':
                n_y = (n_y+dy) % len(board)
                if n_y < 0:
                    n_y += len(board)
                n_x = (n_x+dx) % len(board[n_y])
                if n_x < 0:
                    n_x += len(board[n_y])
            
            if board[n_y][n_x] == '#':
                continue
            
            positions.add((x, y, facing))
            x, y = n_x, n_y
            
print(x, y, facing)
print(1000*(y+1)+4*(x+1)+facing)

# board = [[board[y][x] for x in range(len(board[y]))] for y in range(len(board))]
# facing_rep = ['<', '^', '>', 'v']
# for x, y, f in positions:
#     board[y][x] = facing_rep[f]

# for row in board:
#     print(''.join(row))

