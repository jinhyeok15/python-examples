def solution(numbers, target):
    cnt = _Count()
    _dfs(cnt, numbers, target)
    return cnt.value


class _Count:
    def __init__(self):
        self.value = 0
    def __next__(self):
        self.value += 1
        return self.value


def _dfs(cnt, numbers, target, total=0, curr=0):
    if curr == len(numbers):
        if total == target:
            next(cnt)
        return
    
    for i in (-1, 1):
        _dfs(cnt, numbers, target, total + i*numbers[curr], curr+1)
