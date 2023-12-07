
def get_marker_index(line):
    sets = []
    for i in range(13, len(line)):
        sets.append(set(line[i-13:i+1]))
    
    for i, val in enumerate(sets):
        if(len(val) == 14):
            return i+14

with open('input.txt', 'r') as f:
    arr = [get_marker_index(line) for line in f]

print(arr[0])