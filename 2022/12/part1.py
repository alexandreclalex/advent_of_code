from collections import deque

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            start = (i, j)
        elif lines[i][j] == 'E':
            end=(i, j)


grid = [[ord(x) for x in line] for line in lines]
grid[start[0]][start[1]] = ord('a')
grid[end[0]][end[1]] = ord('z')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = list(zip(dy, dx))

score = [[0]*len(grid[0]) for _ in range(len(grid))]
visited = [[False]*len(grid[0]) for _ in range(len(grid))]
visited[0][0] = True


queue = deque([start])
min_score = None

while queue:
    x, y = queue.pop()
    for dx, dy in directions:
        if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and not visited[x+dx][y+dy]:
            if grid[x+dx][y+dy] - grid[x][y] <= 1:
                if (x+dx, y+dy) == end:
                    print(score[x][y] + 1)
                score[x+dx][y+dy] = score[x][y] + 1
                visited[x+dx][y+dy] = True
                queue.appendleft((x+dx, y+dy))