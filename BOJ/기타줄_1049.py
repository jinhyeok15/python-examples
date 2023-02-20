from bisect import insort

N, M = map(int, input().split())

packages = []
units = []

for _ in range(M):
    pp, up = map(int, input().split())
    insort(packages, pp)
    insort(units, up)

money = 0
money += N // 6 * min(packages[0], units[0]*6)
money += min(N % 6 * units[0], packages[0])

print(money)
