
board = []
with open('input.txt', 'r') as f:
    for row in f:
        board.append([int(x) for x in row[:-1]])
        
print(board)
visible = [[False for x in range(len(board[0]))] for _ in range(len(board))]

def rotate(arr):
    return [list(x) for x in zip(*arr[::-1])]

def find_visible():
    for i in range(len(board)):
        max_height = -1
        for ii in range(len(board[i])):
            if board[i][ii] > max_height:
                max_height = board[i][ii]
                visible[i][ii] = True
                if max_height == 9:
                    break
                
for i in range(4):
    find_visible()
    board = rotate(board)
    visible = rotate(visible)
    
visible_count = 0
for row in visible:
    for value in row:
        if value:
            visible_count += 1
print(visible_count)
                    
                