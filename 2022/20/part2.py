from collections import deque
with open('input.txt', 'r') as f:
    nums = [int(line[:-1]) for line in f]

INPUT_DATA = [(i, int(x)*811589153) for i, x in enumerate(nums)]
num_inputs = len(INPUT_DATA)

d = deque(INPUT_DATA)

for _ in range(10):
    for index, value in INPUT_DATA:
        while True:
            nIndex, _ = d[0]
            if nIndex == index:
                break
            d.rotate(-1)

        nIndex, nValue = d.popleft()
        
        sign = (nValue // abs(nValue) if nValue != 0 else 1)
        d.rotate(abs(nValue)%(num_inputs-1) * sign * -1)
        d.appendleft((nIndex, nValue))

    while True:
        _, nValue = d[0]
        if nValue != 0:
            d.rotate(-1)
        else:
            break

zero_index = 0
while True:
    _, nValue = d[0]
    if nValue != 0:
        d.rotate(-1)
    else:
        break

print(d[1000 % num_inputs][1] + d[2000 % num_inputs][1] + d[3000 % num_inputs][1])