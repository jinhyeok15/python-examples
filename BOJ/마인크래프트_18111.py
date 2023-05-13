N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def get_total_time(graph, h):
    inv = B
    total = 0
    for i in range(N):
        for j in range(M):
            v = graph[i][j]
            if v == h:
                continue
            elif v < h:
                inv -= h-v
                total += h-v
            else:
                inv += v-h
                total += (2*(v-h))
    if inv < 0:
        return None
    return total


answer = float('inf')
height = 0
for h in range(257):
    total_time = get_total_time(graph, h)
    if total_time is not None:
        if answer >= total_time:
            answer = total_time
            height = h

print(answer, height)
