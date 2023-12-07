
def get_marker_index(line):
    sets = []
    for i in range(3, len(line)):
        sets.append(set(line[i-3:i+1]))
    
    for i, val in enumerate(sets):
        if(len(val) == 4):
            return i+4

with open('input.txt', 'r') as f:
    arr = [get_marker_index(line) for line in f]

print(arr[0])