N, M = map(int, input().split())

packages = []
units = []

for _ in range(M):
    pp, up = map(int, input().split())
    packages.append(pp)
    units.append(up)
min_package = min(packages)
min_unit = min(units)

money = 0
money += N // 6 * min(min_package, min_unit*6)
money += min(N % 6 * min_unit, min_package)

print(money)
