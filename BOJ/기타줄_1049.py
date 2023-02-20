from bisect import insort

N, M = map(int, input().split())

packages = []
units = []

for _ in range(M):
    pp, up = map(int, input().split())
    insort(packages, pp)
    insort(units, up)
min_package = packages[0]
min_unit = units[0]

money = 0
money += N // 6 * min(min_package, min_unit*6)
money += min(N % 6 * min_unit, min_package)

print(money)
