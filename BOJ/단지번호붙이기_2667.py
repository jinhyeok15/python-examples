from bisect import insort

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = set()


class _Count:
    def __init__(self):
        self.value = 0
    def __next__(self):
        self.value += 1
        return self.value
    def is_counted(self):
        return self.value != 0


def dfs(curr, count):
    if curr in visited:
        return
    visited.add(curr)

    if graph[curr[0]][curr[1]] == 0:
        return
    next(count)
    pathes = go(curr, N)
    for path in pathes:
        dfs(path, count)


def go(curr, length):
    pathes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for dy, dx in pathes:
        ny, nx = (curr[0]+dy, curr[1]+dx)
        if ny >= length or nx >= length or ny < 0 or nx < 0:
            continue
        result.append((ny, nx))
    return result


if __name__ == "__main__":
    houses = []
    for y in range(N):
        for x in range(N):
            curr = (y, x)
            cnt = _Count()
            dfs(curr, cnt)
            if cnt.is_counted():
                insort(houses, cnt.value)
    print(len(houses))
    for h in houses:
        print(h)
