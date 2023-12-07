
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]

elves = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            elves.add((y, x))
    
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [1, 0, -1, 1, -1, 1, 0, -1]
        
def has_neighbors(elf):
    y, x = elf
    return any([(y+dy[i], x+dx[i]) in elves for i in range(8)])
            
def can_move(point, direction):
    y, x = point
    if direction == 'N':
        return (y-1, x-1) not in elves and (y-1, x) not in elves and (y-1, x+1) not in elves
    elif direction == 'S':
        return (y+1, x-1) not in elves and (y+1, x) not in elves and (y+1, x+1) not in elves
    elif direction == 'W':
        return (y-1, x-1) not in elves and (y, x-1) not in elves and (y+1, x-1) not in elves
    elif direction == 'E':
        return (y-1, x+1) not in elves and (y, x+1) not in elves and (y+1, x+1) not in elves

def next_pos(point, direction):
    y, x = point
    if direction == 'N':
        return (y-1, x)
    elif direction == 'S':
        return (y+1, x)
    elif direction == 'W':
        return (y, x-1)
    elif direction == 'E':
        return (y, x+1)

num_rounds = 99999
directions = ['N', 'S', 'W', 'E']
for _ in range(num_rounds):
    mapping = {}
    need_to_move = set([elf for elf in elves if has_neighbors(elf)])
    if len(need_to_move) == 0:
        break
    for direction in directions:
        moved = set()
        for elf in need_to_move:
            if can_move(elf, direction):
                mapping[elf] = next_pos(elf, direction)
                moved.add(elf)
        need_to_move -= moved
                        
                
    count_instances = {}
    for value in mapping.values():
        if value not in count_instances:
            count_instances[value] = 0
        count_instances[value] += 1
    
    next_elves = set([elf for elf in elves if elf not in mapping])
    for key in mapping:
        value = mapping[key]
        if count_instances[value] == 1:
            next_elves.add(value)
        else:
            next_elves.add(key)
    elves = next_elves
    
    directions = directions[1:] + directions[:1]

x_vals = sorted(elem[1] for elem in elves)
y_vals = sorted(elem[0] for elem in elves)

xmin, xmax = x_vals[0], x_vals[-1]
ymin, ymax = y_vals[0], y_vals[-1]

print(_+1)