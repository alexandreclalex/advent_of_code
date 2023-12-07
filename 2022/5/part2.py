
board_lines = []

instructions = []

with open('input.txt', 'r') as f:
    for line in f:
        if '[' in line:
            board_lines.append(line)
        else:
            instructions.append([token for token in line.split()])

instructions = instructions[2:]

def convert_index(index):
    return 1+4*index

board = []
for i in range(9):
    arr = []
    for line in board_lines:
        char = line[convert_index(i)]
        if char != ' ':
            arr.append(char)
    board.append(arr[::-1])
    
for tokens in instructions:
    iterations = int(tokens[1])
    start = int(tokens[3])-1
    end = int(tokens[5])-1
    stack = []
    for _ in range(iterations):
        val = board[start].pop()
        stack.append(val)
        
    board[end] += stack[::-1]
    

print(''.join([row[-1] for row in board]))