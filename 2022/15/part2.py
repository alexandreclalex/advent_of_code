

with open('input.txt', 'r') as f:
    lines = [line[:-1].split() for line in f]

closest_beacons = dict()
beacon_distances = dict()

min_x , min_y = 0, 0
max_x, max_y = 4_000_000, 4_000_000

# board = [[1]*max_x for _ in range(max_y)]

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for tokens in lines:
    x = int(tokens[2][2:-1])
    y = int(tokens[3][2:-1])
    
    xx = int(tokens[8][2:-1])
    yy = int(tokens[9][2:])
    closest_beacons[(x, y)] = (xx, yy)
    beacon_distances[(x, y)] = distance((x, y), (xx, yy))

for y in range(min_y, max_y+1):
    ranges = []
    
    for sensor in beacon_distances:
        min_dist = beacon_distances[sensor]
        y_dist = abs(sensor[1] - y)
        dx = min_dist - y_dist
        if dx < 0:
            continue
        
        ranges.append((sensor[0] - dx, sensor[0] + dx))
    
    ranges.sort()
    
    compact = []
    low_x, high_x = ranges[0]
    for n_low_x, n_high_x in ranges[1:]:
        if n_low_x-1 <= high_x:
            high_x = max(high_x, n_high_x)
        else:
            compact.append((low_x, high_x))
            low_x, high_x = n_low_x, n_high_x
    compact.append((low_x, high_x))

    if len(compact) != 1:
        (a, b), (c, d) = compact
        x = b+1
        print(x * 4000000 + y)
        break