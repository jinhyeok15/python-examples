import sys

def _dfs(cur, visited, cnt):
    visited.add(cur)

    for i in graph[cur]:
        if i in visited: continue
        cnt = _dfs(i, visited, cnt+1)
    
    return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    cnt = _dfs(1, visited, 0)
    print(cnt)
