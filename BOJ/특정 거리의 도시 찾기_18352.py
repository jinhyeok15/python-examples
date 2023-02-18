from collections import deque
from bisect import insort

N, M, K, X = map(int, input().split())
graph = {i+1:[] for i in range(N)}
result = []

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)

q = deque()
visited = set()
q.append((X, 0))

while q:
    node, dist = q.popleft()
    if dist == K and node not in visited:
        insort(result, node)
        continue
    if dist < K:
        visited.add(node)
        for i in graph[node]:
            q.append((i, dist+1))

if not result:
    print(-1)
else:
    for i in result:
        print(i)
