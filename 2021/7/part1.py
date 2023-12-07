with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().split(',')))

def calculate_cost(index):
    total_cost = 0
    for value in arr:
        total_cost += abs(value - index)
    return total_cost
        
cost_arr = list(map(calculate_cost, range(max(arr)+1)))

print(min(cost_arr))