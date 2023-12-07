from collections import deque
with open('input.txt', 'r') as f:
    nums = [int(line[:-1]) for line in f]

INPUT_DATA = [(i, int(x)) for i, x in enumerate(nums)]
num_inputs = len(INPUT_DATA)

d = deque(INPUT_DATA)

# Part 1
for index, value in INPUT_DATA:
    while True:
        nIndex, _ = d[0]
        if nIndex == index:
            break
        d.rotate(-1)

    nIndex, nValue = d.popleft()
    d.rotate(-1 * nValue)
    d.appendleft((nIndex, nValue))

zero_index = 0
while True:
    _, nValue = d[0]
    if nValue != 0:
        d.rotate(-1)
    else:
        break

print(d[1000 % num_inputs][1] + d[2000 % num_inputs][1] + d[3000 % num_inputs][1])


# order = list(range(len(nums)))
# i = 0

# while i < len(nums):
#     old_index = order.index(i)
#     val = nums[old_index]
#     new_index = (old_index+val)% len(nums)
#     if new_index < 0:
#         new_index += len(nums)
#     if val > 0:
#         nums.insert(new_index, nums.pop(old_index))
#         order.insert(new_index, order.pop(old_index))
#     elif val < 0:
#         nums.insert(new_index-1, nums.pop(old_index))
#         order.insert(new_index-1, order.pop(old_index))
#     i+=1
    
total = 0
offset = nums.index(0)
for i in [1000, 2000, 3000]:
    total += nums[(offset+i) % len(nums)]
print(total)
print(len(nums), len(set(nums)))