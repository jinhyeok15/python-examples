from collections import deque

pathes = [
    (1, 2), (2, 1),
    (-1, 2), (-2, 1),
    (1, -2), (2, -1),
    (-1, -2), (-2, -1)
]


def bfs(start, target, I, visited):
    q = deque()
    q.append((start, 0))

    while q:
        curr, count = q.popleft()
        if curr == target:
            print(count)
            return

        for path in pathes:
            dy, dx = path
            y, x = curr
            if x+dx < 0 or y+dy < 0 or x+dx >= I or y+dy >= I: continue
            _p = (y+dy, x+dx)
            if _p not in visited:
                visited.add(_p)
                q.append((_p, count+1))


_case = int(input())
for _ in range(_case):
    I = int(input())
    start = tuple(map(int, input().split(' ')))
    target = tuple(map(int, input().split(' ')))
    visited = set()
    visited.add(start)
    bfs(start, target, I, visited)
