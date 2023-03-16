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
    cave = []
    for i in range(N):
        cave.append(list(map(int, input().split())))
    
    min_plan = [[float('inf') for _ in range(N)] for _ in range(N)]
    start = (0, 0)
    min_plan[start[0]][start[1]] = cave[start[0]][start[1]]

    queue = [(cave[start[0]][start[1]], start)]
    while queue:
        v, curr = heapq.heappop(queue)

        if min_plan[curr[0]][curr[1]] < v:
            continue

        for path in go(curr, N):
            y, x = path
            acc = v+cave[y][x]

            if acc < min_plan[y][x]:
                min_plan[y][x] = acc
                heapq.heappush(queue, (acc, path))

    print(f"Problem {cnt}: {min_plan[N-1][N-1]}")
    cnt += 1
