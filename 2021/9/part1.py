
arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append([10] + list(map(int, line[:-1])) + [10])

arr.insert(0, [10]*len(arr[0]))
arr.append(arr[0].copy())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = list(zip(dx, dy))

total_risk = 0
for i in range(1,len(arr)-1):
    for ii in range(1, len(arr[i])-1):
        for dx, dy in directions:
            if arr[i+dx][ii+dy] <= arr[i][ii]:
                break
        else:
            total_risk += 1 + arr[i][ii]

print(total_risk)