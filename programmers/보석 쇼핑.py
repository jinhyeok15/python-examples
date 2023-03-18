from collections import deque
import heapq


def solution(gems):
    heap = []
    category = set(gems)
    
    q = deque([(0, gems[0])])
    for i, gem in enumerate(gems):
        item = q.popleft()
        if item[1] == gem:
            q.append((i, gem))
        else:
            q.append((i, gem)); q.appendleft(item)
        frozen = list(q)
        if set(gems[frozen[0][0]:frozen[-1][0]+1]) == category:
            heapq.heappush(heap, preprocess_heap_data(q.copy()))

    return get_layer(heapq.heappop(heap)[1])


def get_layer(q):
    if len(q) > 1:
        start, end = q.popleft()[0], q.pop()[0]
    elif len(q) == 1:
        item = q.popleft()
        start, end = item[0], item[0]
    else:
        raise Exception()
    return [start+1, end+1]


def preprocess_heap_data(q):
    item = q.popleft()
    if not q:
        q.appendleft(item)
        return (len(q), q)
    comp = q.popleft()
    if item[1] == comp[1]:
        q.appendleft(comp)
        return (len(q), q)
    q.appendleft(comp); q.appendleft(item); return (len(q), q)
