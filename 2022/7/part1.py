
class file:
    def __init__(self, size) -> None:
        self.size = size

class dir:
    def __init__(self) -> None:
        self.data = {}
        self.parent = None
    
    def add(self, obj, name):
        self.data[name] = obj
        if isinstance(obj, dir):
            obj.parent = self
    
    def get_size_r(self):
        total = 0
        for obj in self.data.values():
            if isinstance(obj, dir):
                total += obj.get_size_r()
            elif isinstance(obj, file):
                total += obj.size
        return total


with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]

root_dir = dir()
current_dir = root_dir
dir_list = []
index = 1
while index < len(lines):
    if lines[index] == '$ ls':
        index += 1
        while lines[index][0] != '$':
            x, name = lines[index].split()
            if x == 'dir':
                new_dir = dir()
                dir_list.append(new_dir)
                current_dir.add(new_dir, name)
            else:
                current_dir.add(file(int(x)), name)
            index += 1
            if index >= len(lines):
                break
    elif lines[index].startswith('$ cd'):
        next_dir = lines[index][5:]
        if next_dir == '..':
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.data[next_dir]
        index += 1


sizes = [x.get_size_r() for x in dir_list]
print(sum([size for size in sizes if size <= 100000]))