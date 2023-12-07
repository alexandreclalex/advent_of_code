
calories = []

with open('input.txt', 'r') as f:
    
    curr_calories = 0
    for line in f:
        if line == '\n':
            calories.append(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line[:-1])
            
print(max(calories))
