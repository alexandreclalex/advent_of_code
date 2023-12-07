
board = []
with open('input.txt', 'r') as f:
    for row in f:
        board.append([int(x) for x in row[:-1]])
        
score = [[1 for x in range(len(board[1]))] for _ in range(len(board))]

def rotate(arr):
    return [list(x) for x in zip(*arr[::-1])]

def get_score():
    for i in range(len(board)):
        for ii in range(len(board[i])):
            for iii in range(ii-1, -1, -1):
                if board[i][iii] >= board[i][ii]:
                    score[i][ii]*=(ii-iii)
                    break
            else:
                score[i][ii]*=(ii)
                
for i in range(4):
    get_score()
    board = rotate(board)
    score = rotate(score)
    

print(max([max(row)for row in score]))
                