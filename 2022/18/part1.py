
with open('input.txt', 'r') as f:
    dims = [tuple(map(int, line[:-1].split(','))) for line in f]

def is_adj(a, b):
    face_diff = [a[i] - b[i] for i in range(3)]
    return len([x for x in face_diff if x == 0]) == 2 and abs(sum(face_diff)) <= 1

num_adj = 0
for i in range(len(dims)-1):
    for j in range(i+1, len(dims)):
        if is_adj(dims[i], dims[j]):
            num_adj += 1

print(6*len(dims) - 2*num_adj)