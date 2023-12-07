with open('input.txt', 'r') as f:
    arr = [line.split() for line in f]
    horizontal, depth = 0, 0
    for direction, value in arr:
        value = int(value)
        if direction == 'forward':
            horizontal += value
        elif direction == 'up':
            depth -= value
        else:
            depth += value
    print(horizontal, depth, horizontal*depth)