
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]

sand_origin = (500, 0)

R = set()
for line in lines:
    points = [list(map(int, x.split(','))) for x in line.split(' -> ')]
    for i in range(len(points)-1):
        start = points[i]
        end = points[i+1]
        if end[0] < start[0] or end[1] < start[1]:
            start, end = end, start
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                R.add((x, y))

floor = 2+max(r[1] for r in R)
lo_x = min(r[0] for r in R)-2000
hi_x = max(r[0] for r in R)+2000
for x in range(lo_x, hi_x):
    R.add((x,floor))


for t in range(1000000000):
    rock = (500, 0)
    while True:
        if (rock[0],rock[1]+1) not in R:
            rock = (rock[0],rock[1]+1)
        elif (rock[0]-1,rock[1]+1) not in R:
            rock = (rock[0]-1, rock[1]+1)
        elif (rock[0]+1, rock[1]+1) not in R:
            rock = (rock[0]+1, rock[1]+1)
        else:
            break
    if rock == (500, 0):
        print(t+1)
        break
    R.add(rock)