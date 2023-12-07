

connections = dict()

with open('input.txt', 'r') as f:
    for line in f:
        tokens = line[:-1].split('-')
        for i in range(2):
            if tokens[i] not in connections:
                connections[tokens[i]] = []
        connections[tokens[0]].append(tokens[1])
        connections[tokens[1]].append(tokens[0])
        
major = set([conn for conn in connections if conn.upper() == conn])
minor = set([conn for conn in connections if conn.lower() == conn])
minor.remove('start')
paths = set()

def search(path):
    if path[-1] == 'end':
        paths.add(path)
        return
    
    minor_counts = {}
    has_visited_twice = False
    for elem in minor:
        minor_counts[elem] = 0
    for elem in path:
        if elem in minor:
            minor_counts[elem] += 1
            if minor_counts[elem] == 2:
                has_visited_twice = True
    
    for connection in connections[path[-1]]:
        if (connection in minor and minor_counts[connection] >= 1 and has_visited_twice) or connection == 'start':
            pass
        else:
            search(path + tuple([connection]))
            

initial_path = 'start'
search(tuple([initial_path]))
print(len(paths))