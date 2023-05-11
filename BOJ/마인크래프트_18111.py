N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 최소와 최대 높이를 구한다.
max_h, min_h = 0, 256
sorted_by_h = []
for i in range(N):
    for j in range(M):
        v = graph[i][j]
        min_h = min(v, min_h)
        max_h = max(v, max_h)
        sorted_by_h.append(v)
sorted_by_h.sort(reverse=True)


def get_total_time(columns, graph, h):
    inv = B
    total = 0
    for v in columns:
        if v == h:
            continue
        elif v < h:
            if inv >= h-v:
                inv -= h-v
                total += h-v
            else:
                return None
        else:
            inv += v-h
            total += (2*(v-h))
    return total


answer = float('inf')
height = 0
for h in range(min_h, max_h+1):
    total_time = get_total_time(sorted_by_h, graph, h)
    if total_time is not None:
        if answer >= total_time:
            answer = total_time
            height = h

print(*[answer, height])
