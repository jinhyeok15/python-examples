import heapq


def go(path, N):
    y, x = path
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    results = []
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        results.append((ny, nx))

    return results


cnt = 1
while True:
    N = int(input())
    if N == 0: break

    graph = {}
    for i in range(N):
        for j, v in enumerate(list(map(int, input().split()))):
            graph[(i, j)] = [v, float('inf')]

    start = (0, 0)
    graph[start][1] = graph[start][0]

    queue = [(graph[start][0], start)]
    while queue:
        v, curr = heapq.heappop(queue)

        if graph[curr][1] < v:
            continue

        for path in go(curr, N):
            y, x = path
            
            acc = v+graph[path][0]
            if acc < graph[path][1]:
                graph[path][1] = acc
                heapq.heappush(queue, (acc, path))

    print(f"Problem {cnt}: {graph[(N-1, N-1)][1]}")
    cnt += 1
