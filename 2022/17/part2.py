
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

# def print_board():
#     for row in board[-min(max_height+1, 100):][::-1]:
#         print(''.join(['@' if x ==1 else '.' for x in row]))
#
# while num_rocks_fallen < 2022:
#     rock = rocks[num_rocks_fallen % len(rocks)]
#     positions = [[x+2, y+max_height + 3] for x, y in rock]
#     board += [[0]* (max_height - len(board) + 7)]
#     can_move_lateral = True
#     can_move_vertical = True
#     while can_move_vertical:
#         dx = 1 if wind[wind_index] == '>' else -1
#         wind_index += 1
#         wind_index %= len(wind)
#         dy = -1
        
#         # Check if we can move with wind
#         for x, y in positions:
#             if x+dx >=7 or x+dx < 0 or board[y][x+dx] == 1:
#                 can_move_lateral = False
#                 break
#         else:
#             can_move_lateral = True

#         # Move with wind
#         if can_move_lateral:
#             # print('Moving Right' if dx >0 else 'Moving Left')
#             for i in range(len(positions)):
#                 positions[i][0] += dx
#         # else:
#         #     print('Cannot Move Right' if dx >0 else 'Cannot Move Left')
                
        
#         # Check if we can move down
#         for x, y in positions:
#             if y+dy < 0 or board[y+dy][x] == 1:
#                 can_move_vertical = False
#                 break
#         else:
#             can_move_vertical = True
        
#         # Move down
#         if can_move_vertical:
#             # print('Moving Down')
#             for i in range(len(positions)):
#                 positions[i][1] += dy
#         # else:
#         #     print('Came to Rest')
        
                
#     # Place on board:
#     for x, y in positions:
#         board[y][x] =1
#         if y+1 > max_height:
#             max_height = y+1
#     num_rocks_fallen += 1

board = set([(x, 0) for x in range(7)])

def uid(board):
    # Create Snapshot of top 30 rows
    max_y = max([y for x, y in board])
    return frozenset([(x, max_y - y) for x, y in board if max_y-y<=30])

seen = {}
top = 0
wind_index = 0
num_rocks_fallen = 0
added = 0
L = 1_000_000_000_000
while num_rocks_fallen < L:
    rock = rocks[num_rocks_fallen%5]
    positions = set([(x+2, y+top + 4) for x, y in rock])
    while True:
        dx = 1 if wind[wind_index] == '>' else -1
        wind_index += 1
        wind_index %= len(wind)
        dy = -1
        
        # Check if we can move with wind
        for x, y in positions:
            if x+dx >=7 or x+dx < 0 or (x+dx, y) in board:
                can_move_lateral = False
                break
        else:
            can_move_lateral = True

        # Move with wind
        if can_move_lateral:
            positions = set([(x+dx, y) for x, y in positions])             
        
        # Check if we can move down
        for x, y in positions:
            if y+dy < 0 or (x, y+dy) in board:
                can_move_vertical = False
                break
        else:
            can_move_vertical = True
        
        # Move down
        if can_move_vertical:
            positions = set([(x, y+dy) for x, y in positions])
        else:
            board |= positions
            top = max([y for x, y in positions]+[top])
            
            row_uid = (wind_index, num_rocks_fallen%5, uid(board))
            if row_uid in seen and num_rocks_fallen > 2022:
                (old_num_rocks_fallen, old_top) = seen[row_uid]
                dy = top - old_top
                dn_r_f = num_rocks_fallen - old_num_rocks_fallen
                amount = (L - num_rocks_fallen)//dn_r_f
                added += amount*dy
                num_rocks_fallen += amount*dn_r_f
                assert num_rocks_fallen <= L
            seen[row_uid] = (num_rocks_fallen, top)
            break
    num_rocks_fallen += 1
    if num_rocks_fallen==2022:
        print(top)
print(top+added)