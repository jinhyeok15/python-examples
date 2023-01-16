n, h = map(int, input().split(" "))

# 누적합 이용
lines = [0] * h

for i in range(n):
    high = int(input())
    # 석순
    if i % 2 == 0:
        lines[h - high] += 1
    # 종유석
    else:
        lines[0] += 1
        lines[high] -= 1

for i in range(1, h):
    lines[i] += lines[i - 1]


print(lines)
