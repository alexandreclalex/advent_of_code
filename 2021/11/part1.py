ITERATIONS = 100


with open('input.txt', 'r') as f:
    board = [list(map(int, line[:-1])) for line in f]

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
directions = list(zip(dx, dy))

def get_flashers():
    flashers = []
    for i in range(len(board)):
        for ii in range(len(board[i])):
            if board[i][ii] >= 10:
                flashers.append((i, ii))
    return flashers

flash_count = 0

for _ in range(ITERATIONS):
    for i in range(len(board)):
        for ii in range(len(board[i])):
            board[i][ii] += 1
    flashed = set()
    flashers = get_flashers()
    while len(flashers) > 0:
        for x, y in flashers:
            flashed.add((x, y))
            for dx, dy in directions:
                if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[x+dx]):
                    board[x+dx][y+dy] += 1
        flashers = [t for t in get_flashers() if t not in flashed]
    
    for x, y in flashed:
        flash_count += 1
        board[x][y] = 0

    
print(flash_count)
