N = int(input())
group = [int(i) for i in input().split()]
group.sort(reverse=True)

curr = 0
count = 0
for i in range(len(group)):
    cursor = i
    if group[cursor] == curr: continue

    tmp_count = 0
    while cursor < len(group):
        fear = group[cursor]
        cursor += fear
        if cursor > len(group): break
        tmp_count += 1
        if cursor == len(group): continue
        fear = group[cursor]

    count = max(count, tmp_count)
    curr = group[i]

print(count)
