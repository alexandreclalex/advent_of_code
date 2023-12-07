with open("input.txt", 'r') as f:
	arr = [int(line.rstrip()) for line in f]
	greater_than = [1 if arr[i] > arr[i-1] else 0 for i in range(1, len(arr))]
	print(sum(greater_than))
