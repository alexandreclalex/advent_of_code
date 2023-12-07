
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    wind = lines[0]


rocks = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (2, 1), (1, 2), (1, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1))
    ]

board = [[0]*7 for _ in range(100000)]
max_height = 0

def print_board():
    for row in board[:max_height+1][::-1]:
        print(''.join(['@' if x ==1 else '.' for x in row]))

wind_index = 0
num_rocks_fallen = 0

while num_rocks_fallen < 2022:
    rock = rocks[num_rocks_fallen % len(rocks)]
    positions = [[x+2, y+max_height + 3] for x, y in rock]
    can_move_lateral = True
    can_move_vertical = True
    while can_move_vertical:
        dx = 1 if wind[wind_index] == '>' else -1
        wind_index += 1
        wind_index %= len(wind)
        dy = -1
        
        # Check if we can move with wind
        for x, y in positions:
            if x+dx >=7 or x+dx < 0 or board[y][x+dx] == 1:
                can_move_lateral = False
                break
        else:
            can_move_lateral = True

        # Move with wind
        if can_move_lateral:
            # print('Moving Right' if dx >0 else 'Moving Left')
            for i in range(len(positions)):
                positions[i][0] += dx
        # else:
        #     print('Cannot Move Right' if dx >0 else 'Cannot Move Left')
                
        
        # Check if we can move down
        for x, y in positions:
            if y+dy < 0 or board[y+dy][x] == 1:
                can_move_vertical = False
                break
        else:
            can_move_vertical = True
        
        # Move down
        if can_move_vertical:
            # print('Moving Down')
            for i in range(len(positions)):
                positions[i][1] += dy
        # else:
        #     print('Came to Rest')
        
                
    # Place on board:
    for x, y in positions:
        board[y][x] =1
        if y+1 > max_height:
            max_height = y+1
    num_rocks_fallen += 1
    

    
print(max_height)
# print_board()