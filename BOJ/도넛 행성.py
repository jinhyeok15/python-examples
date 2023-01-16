import sys
sys.setrecursionlimit(100000)


N, M = tuple(map(int, sys.stdin.readline().split(' ')))
info = []
for _ in range(N):
    info.append(list(map(int, sys.stdin.readline().split(' '))))

visited = {}
def dfs(current):
    if info[current[0]][current[1]] == 1:
        return 0
    visited[f"{current[0]} {current[1]}"] = True
    pathes = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for path in pathes:
        y, x = go(current, path, N, M)
        if info[y][x] == 1:
            continue
        if visited[f"{y} {x}"]:
            continue
        dfs((y, x))
    return 1


def go(current, path, N, M):
    y, x = current[0] + path[0], current[1] + path[1]
    if y < 0: y = N-1
    elif y == N: y = 0
    if x < 0: x = M-1
    elif x == M: x = 0
    return y, x
