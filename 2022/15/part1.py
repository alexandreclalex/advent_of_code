

with open('input.txt', 'r') as f:
    lines = [line[:-1].split() for line in f]
    
closest_beacons = dict()
beacon_distances = dict()

min_test_x , min_test_y = 10**100, 10**100
max_test_x, max_test_y = -1*10*100, -1*10*100 

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for tokens in lines:
    x = int(tokens[2][2:-1])
    y = int(tokens[3][2:-1])
    
    xx = int(tokens[8][2:-1])
    yy = int(tokens[9][2:])
    closest_beacons[(x, y)] = (xx, yy)
    beacon_distances[(x, y)] = distance((x, y), (xx, yy))
    
for sensor in closest_beacons:
    min_test_x = min((sensor[0] - closest_beacons[sensor][0], min_test_x))
    max_test_x = max((sensor[0] + closest_beacons[sensor][0], max_test_x))
    
impossible_points = set()
row = 2_000_000
for i in range(min_test_x-1, max_test_x+1):
    for sensor in beacon_distances:
        if distance(sensor, (i, row)) <= beacon_distances[sensor]:
            impossible_points.add((i, row))
            break
        
for beacon in closest_beacons.values():
    if beacon in impossible_points:
        impossible_points.remove(beacon)
print(len(impossible_points))