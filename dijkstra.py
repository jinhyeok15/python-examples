import heapq


def dijkstra(graph, start):
    """
    graph = {
    (0, 0): {(0, 1): 2, (1, 0): 5},
    (0, 1): {(0, 0): 2, (0, 2): 7, (1, 1): 3},
    (0, 2): {(0, 1): 7, (1, 2): 1},
    (1, 0): {(0, 0): 5, (2, 0): 4, (1, 1): 6},
    (1, 1): {(0, 1): 3, (1, 0): 6, (1, 2): 4, (2, 1): 2},
    (1, 2): {(0, 2): 1, (1, 1): 4, (2, 2): 3},
    (2, 0): {(1, 0): 4, (2, 1): 5},
    (2, 1): {(1, 1): 2, (2, 0): 5, (2, 2): 1},
    (2,
    """
    min_plan = {node: float('inf') for node in graph}  # start로부터 거리 값을 저장하기 위함
    min_plan[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, (min_plan[start], start))

    while queue:
        v, curr = heapq.heappop(queue)

        # 기존의 거리보다 더 긴 경로를 찾은 경우 무시
        if min_plan[curr] < v:
            continue

        for node, w in graph[curr].items():
            acc = v + w

            # 더 짧은 경로를 찾은 경우, 거리 값을 업데이트
            if acc < min_plan[node]:
                min_plan[node] = acc
                heapq.heappush(queue, (acc, node))

    return min_plan
