N, M, I = map(int, input().split())
board = {}
for i in range(N):
    for j, h in enumerate(map(int, input().split())):
        board[(i, j)] = h


class Work:
    def __init__(self, inventory, board):
        self.inventory = inventory
        self.board = board
        self.time = 0
    
    def remove(self, path):
        if self.board[path] == 0:
            return 0
        self.board[path] -= 1
        self.inventory += 1
        self.time += 2
        return 1
    
    def push(self, path):
        if self.board[path] == 256:
            return 0
        if self.inventory == 0:
            return 0
        self.board[path] += 1
        self.inventory -= 1
        self.time += 1
        return 1

    def is_flat(self):
        return len(set(self.board.values())) == 1
    
    @property
    def max_height(self):
        return max(self.board.values())
    
    @property
    def min_height(self):
        return min(self.board.values())


w = Work(I, board)

while not w.is_flat():
    min_keys = [key for key, value in w.board.items() if value == w.min_height]
    max_keys = [key for key, value in w.board.items() if value == w.max_height]

    flag = False
    if len(max_keys) * 2 >= len(min_keys):
        if w.inventory >= len(min_keys):
            for key in min_keys:
                sts = w.push(key)
                if sts == 0:
                    flag = True; break
        if flag: break
    else:
        for key in max_keys:
            sts = w.remove(key)
            if sts == 0:
                flag = True; break
        if flag: break

print(*[w.time, w.max_height])
