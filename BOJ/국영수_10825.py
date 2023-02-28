import heapq

N = int(input())
array = []

for i in range(N):
    _name, _ko, _en, _math = tuple(input().split())
    heapq.heappush(array, (-int(_ko), int(_en), -int(_math), _name))

while array:
    print(heapq.heappop(array)[3])
