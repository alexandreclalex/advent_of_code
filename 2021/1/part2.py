with open("input.txt", 'r') as f:
    raw_arr = [int(line.rstrip()) for line in f]
    arr = [sum(raw_arr[i:i+3]) for i in range(len(raw_arr)-2)] + [raw_arr[-2] + raw_arr[-1], raw_arr[-1]]
    greater_than = [1 if arr[i] > arr[i-1] else 0 for i in range(1, len(arr))]
    print(sum(greater_than))