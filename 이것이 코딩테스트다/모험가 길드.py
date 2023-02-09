N = int(input())
group = [int(i) for i in input().split()]
group.sort(reverse=True)

curr = 0
count = 0
for i in range(len(group)):
    cursor = i
    fear = group[cursor]
    if fear == curr: continue

    tmp_count = 0
    while cursor < len(group):
        if cursor + fear > len(group): break
        cursor += fear
        fear = group[cursor]
        tmp_count += 1

    count = max(count, tmp_count)
    curr = group[i]

print(count)
