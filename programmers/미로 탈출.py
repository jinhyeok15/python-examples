import heapq
from collections import defaultdict


def solution(n, start, end, roads, traps):
    graph = defaultdict(dict)
    rgraph = defaultdict(dict)
    for i, j, s in roads:
        graph[i][j] = s
        rgraph[j][i] = s

    min_plan = {node: float('inf') for node in range(1, n+1)}
    min_plan[start] = 0
    queue = []
    heapq.heappush(queue, (min_plan[start], start, 1))

    while queue:
        s, curr, status = heapq.heappop(queue)
        
        if s > min_plan[curr]:
            continue
        
        if curr == end:
            break
        
        if status == 1:
            _graph = graph
        else:
            _graph = rgraph
        
        for node, w in _graph[curr].items():
            acc = s+w
            
            if acc < min_plan[node]:
                min_plan[node] = acc
                item = (acc, node, status) if node not in traps else (acc, node, -status)
                heapq.heappush(queue, item)

    return min_plan[end]
