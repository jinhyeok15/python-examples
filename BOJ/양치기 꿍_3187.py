import sys
from typing import Optional
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(100000)

R, C = tuple(map(int, input().split(' ')))
farm = []
for _ in range(R):
    farm.append(list(input()))


def _dfs(current, visited: dict, record, counter: defaultdict) -> Optional[defaultdict]:
    y, x = current
    _key = f"{y} {x}"
    if _key in visited: return
    if farm[y][x] == "#": return

    visited[_key] = True
    if farm[y][x] != ".":
        counter[farm[y][x]] += 1

    pathes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for path in pathes:
        _next = go(current, path, R, C)
        if _next is None: continue
        _dfs(_next, visited, record, counter)


def go(current, path, max_row, max_col) -> Optional[tuple]:
    y, x = current
    dy, dx = path
    if dy != 0:
        if y+dy < 0: return None
        if y+dy >= max_row: return None
    if dx != 0:
        if x+dx < 0: return None
        if x+dx >= max_col: return None
    return (y+dy, x+dx)


record = [0, 0]  # [k, v]
visited = {}
for r in range(R):
    for c in range(C):
        _key = f"{r} {c}"

        if _key in visited: continue
        counter = defaultdict(int)
        _dfs((r, c), visited, record, counter)
        
        if counter["v"] >= counter["k"]:
            record[1] += counter["v"]
        else:
            record[0] += counter["k"]

print(f"{record[0]} {record[1]}")
