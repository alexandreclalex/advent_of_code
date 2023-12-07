import re

line_pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')

class Vent_Line:
    def __init__(self, line) -> None:
        self.line = line
        self.start, self.end = self.parse_line(line)
        
    def parse_line(self, line):
        matched = line_pattern.match(line)
        groups = [int(group) for group in matched.groups()]
        return ((groups[0], groups[1]), (groups[2], groups[3]))
        
    def __repr__(self) -> str:
        return str(self.start) + ', ' + str(self.end)
    
    def get_line_indices(self):
        indices = []
        if self.start[0] != self.end[0] and self.start[1] != self.end[1]:
            # Do not process lines that are not horizontal or vertical
            return []
        else:
            current_location = self.start
            indices.append(current_location)
            while current_location != self.end:
                delta = [self.end[i] - current_location[i] for i in range(2)]
                step = [delta[i]//abs(delta[i]) if delta[i] != 0 else 0 for i in range(2)]
                current_location = tuple([current_location[i] + step[i] for i in range(2)])
                indices.append(current_location)
            return indices
        


with open('input.txt', 'r') as f:
    vent_lines = [Vent_Line(line) for line in f]

grid = [[0]*1000 for _ in range(1000)]

for line in vent_lines:
    indices = line.get_line_indices()
    for index in indices:
        grid[index[0]][index[1]] += 1




count = 0
for row in grid:
    for value in row:
        if value > 1:
            count += 1
            
print(count)