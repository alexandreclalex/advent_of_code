
with open('input.txt', 'r') as f:
    txt = f.read()
    point_lines, instr_lines = txt.split('\n\n')
    
points = [list(map(int, x.split(','))) for x in point_lines.split()]

def fold(axis, value):
    for i, point in enumerate(points):
        if point[axis] > value:
            point[axis] = 2*value - point[axis]
            
for line in instr_lines.split('\n')[:-1]:
    axis, value = line.split()[2].split('=')
    if axis == 'x':
        fold(0, int(value))
    else:
        fold(1, int(value))
        
        
points_set = set([tuple(p) for p in points])
# Each letter is 5*6
for i in range(6):
    for j in range(40):
        if (j, i) in points_set:
            print('#', end = '')
        else:
            print(' ', end='')
    print()

print(len(points_set))