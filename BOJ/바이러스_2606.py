from collections import deque

N = int(input())
M = int(input())

graph = {i+1:[] for i in range(N)}
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visited = set()
visited.add(1)

q = deque()
q.append((1, visited))
while q:
    start, _visited = q.popleft()
    for n in graph[start]:
        if n in _visited:
            continue
        _visited.add(n)
        q.append((n, _visited))

print(len(visited) - 1)
