import heapq

def dijkstra(graph, start, default=0):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = default
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
                
    return dist

def solution(cave):
    n = len(cave)
    graph = [[] for _ in range(n*n)]
    
    for i in range(n):
        for j in range(n):
            if i > 0:
                graph[n*i+j].append((n*(i-1)+j, cave[i-1][j]))
            if i < n-1:
                graph[n*i+j].append((n*(i+1)+j, cave[i+1][j]))
            if j > 0:
                graph[n*i+j].append((n*i+j-1, cave[i][j-1]))
            if j < n-1:
                graph[n*i+j].append((n*i+j+1, cave[i][j+1]))
                
    dist = dijkstra(graph, 0, cave[0][0])
    return dist[n*n-1]


cnt = 1
while True:
    N = int(input())
    if N == 0: break
    cave = []
    for i in range(N):
        cave.append(list(map(int, input().split())))
    print(f"Problem {cnt}: {solution(cave)}")
    cnt += 1
