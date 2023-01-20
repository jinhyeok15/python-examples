import heapq

N, K = map(int, input().split(' '))

gems = []
for _ in range(N):
    heapq.heappush(gems, (tuple(map(int, input().split(' ')))))  # M, V

backpacks = []
for _ in range(K):
    heapq.heappush(backpacks, int(input()))

ans = 0
tmp_store = []  # 보석의 value 순으로 (-V, M)
while backpacks:
    c = heapq.heappop(backpacks)

    while gems and c >= gems[0][0]:
        gem = heapq.heappop(gems)
        heapq.heappush(tmp_store, (-1 * gem[1]))        
    if tmp_store:
        ans -= heapq.heappop(tmp_store)
    elif not gems:
        break

print(ans)
