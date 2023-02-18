from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F+1)
visited[S] = True

q = deque()
q.append((S, 0))

answer = 'use the stairs'
while q:
    curr, cnt = q.popleft()
    if curr == G:
        answer = cnt
        break

    if curr + U <= F and not visited[curr+U]:
        visited[curr+U] = True
        q.append((curr+U, cnt+1))
    if curr - D > 0 and not visited[curr-D]:
        visited[curr-D] = True
        q.append((curr-D, cnt+1))

print(answer)
