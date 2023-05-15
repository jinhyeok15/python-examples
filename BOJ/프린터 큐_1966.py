import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    q = deque([(i, int(s)) for i, s in enumerate(input().split())])
    count = 0

    while q[m] in q:
        idx, v = q.popleft()
        count += 1

        if not q: break
        
        max_ = max(q, key=lambda x: x[1])[1]
        if v < max_:
            q.append((idx, v))
            count -= 1
        else:
            continue

    print(count)
