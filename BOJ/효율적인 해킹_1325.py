from collections import deque
import sys

input = sys.stdin.readline


def bfs(num):
    q = deque()
    q.append(num)
    visited = [False] * (N+1)
    visited[num] = True
    last = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i]:
                continue
            last += 1
            q.append(i)
            visited[i] = True
    return last


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[j].append(i)

ans = []
maxcnt = 0

for i in range(1, N+1):
    cnt = bfs(i)
    if maxcnt < cnt:
        ans = [i]
        maxcnt = cnt
    elif maxcnt == cnt:
        ans.append(i)

print(*ans)
