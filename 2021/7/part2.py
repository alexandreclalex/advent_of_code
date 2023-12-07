with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().split(',')))

distance_costs = [0]
for i in range(1, max(arr)+1):
    distance_costs.append(distance_costs[i-1]+i)

def calculate_cost(index):
    total_cost = 0
    for value in arr:
        total_cost += distance_costs[abs(value - index)]
    return total_cost
        
cost_arr = list(map(calculate_cost, range(max(arr)+1)))

print(min(cost_arr))