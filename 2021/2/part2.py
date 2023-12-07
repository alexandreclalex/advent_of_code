with open('input.txt', 'r') as f:
    arr = [line.split() for line in f]
    horizontal, depth, aim = 0, 0, 0
    for direction, value in arr:
        value = int(value)
        if direction == 'forward':
            horizontal += value
            depth += value*aim
        elif direction == 'up':
            aim -= value
        else:
            aim += value
    print(horizontal, depth, horizontal*depth)