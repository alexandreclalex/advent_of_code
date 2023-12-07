
with open('input.txt', 'r') as f:
    dims = set([tuple(map(int, line[:-1].split(','))) for line in f])

num_adj = {}
for dim in dims:
    num_adj[dim] = 0
    
def is_adj(a, b):
    face_diff = [a[i] - b[i] for i in range(3)]
    return len([x for x in face_diff if x == 0]) == 2 and abs(sum(face_diff)) <= 1

# for i in range(len(dims)-1):
#     for j in range(i+1, len(dims)):
#         if is_adj(dims[i], dims[j]):
#             num_adj[dims[i]] += 1
#             num_adj[dims[j]] += 1
            
# has_surface = set((x for x in num_adj if num_adj[x] < 6))
# print('Reduced number of dim from', len(dims), 'to', len(has_surface))

directions = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
)

max_dim = max([max([x[i] for x in dims]) for i in range(3)]) + 1
min_dim = min([min([x[i] for x in dims]) for i in range(3)]) - 1

queue = [(0, 0, 0)]
fill = set()
while queue:
    next = queue.pop()
    x, y, z = next
    fill.add(next)
    for dx, dy, dz in directions:
        if min_dim <= x+dx < max_dim and min_dim <= y+dy < max_dim  and min_dim <= z + dz < max_dim:
            if (x+dx, y+dy, z+dz) not in fill and (x+dx, y+dy, z+dz) not in dims:
                queue.append((x+dx, y+dy, z+dz))
                
fill = list(fill)
fill_adj = -1
for i in range(len(fill)-1):
    for j in range(i+1, len(fill)):
        if is_adj(fill[i], fill[j]):
            fill_adj += 1
            
total_fill_SA = 6*len(fill) - 2*fill_adj
exterior_fill_SA = 6*((max_dim - min_dim)**2)
print(total_fill_SA - exterior_fill_SA)