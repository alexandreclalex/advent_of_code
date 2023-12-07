board_dim = 5
with open('input.txt', 'r') as f:
    calls = [int(x) for x in f.readline().split(',')]
    raw_boards = f.readlines()

class Board:
    def __init__(self, arr) -> None:
        self.arr = [[int(x) for x in row.split()] for row in arr]
        self.values = set.union(*map(set, self.arr))
        self.win_sets = []
        self.winning_set = None
        self._find_win_sets()
        
    def _find_win_sets(self) -> None:
        for row in self.arr:
            self.win_sets.append(set(row))
        
        for row in zip(*self.arr):
            self.win_sets.append(set(row))
            
        self.win_sets.append(set([self.arr[i][i] for i in range(board_dim)]))
        self.win_sets.append(set([self.arr[i][-i] for i in range(board_dim)]))
    
    def is_winner(self, calls) -> bool:
        for win_set in self.win_sets:
            if win_set.issubset(calls):
                self.winning_set = win_set
                return True
        return False
        
boards = [Board(raw_boards[i:i+5]) for i in range(1, len(raw_boards), 6)]

for i in range(5, len(calls)):
    called_nums = set(calls[:i+1])
    boards = [board for board in boards if not board.is_winner(called_nums)]
    if len(boards) == 1:
        last_board = boards[0]
    elif len(boards) == 0:
        sum_of_unmarked = sum(last_board.values - called_nums)
        print(sum_of_unmarked * calls[i])
        break