from itertools import chain
from collections import Counter

arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append([10] + list(map(int, line[:-1])) + [10])

arr.insert(0, [10]*len(arr[0]))
arr.append(arr[0].copy())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = list(zip(dx, dy))

low_points = []
for i in range(1,len(arr)-1):
    for ii in range(1, len(arr[i])-1):
        for dx, dy in directions:
            if arr[i+dx][ii+dy] <= arr[i][ii]:
                break
        else:
            low_points.append((i, ii))

visited = [[None]*len(arr[i]) for i in range(len(arr))]

for i, point in enumerate(low_points):
    to_visit = [point]
    while to_visit:
        x, y = to_visit.pop()
        visited[x][y] = i
        for dx, dy in directions:
            if arr[x+dx][y+dy] < 9 and visited[x+dx][y+dy] is None:
                to_visit.append((x+dx, y+dy))
                
counts = Counter(chain.from_iterable(visited))

result = 1
for key, val in counts.most_common(4)[1:]:
    result *= val
print(result)

