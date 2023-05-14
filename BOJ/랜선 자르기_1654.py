# K, N = 1, 1
# lines = [2]

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]


def count_line_unit(unit_length, lines):
    if unit_length == 0:
        return None
    cnt = 0
    for line in lines:
        cnt += line // unit_length
    return cnt


lo = 1
hi = max(lines)

while lo <= hi:
    mid = (lo + hi) // 2
    unit = count_line_unit(mid, lines)
    if unit < N:
        hi = mid - 1
    else:
        lo = mid + 1

print(hi)
