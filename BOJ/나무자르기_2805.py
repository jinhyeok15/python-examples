N, M = map(int, input().split())
heights = sorted([int(s) for s in input().split()], reverse=True)


def get_more_height(need, target_tree):
    moreh = 0
    while True:
        value = target_tree * moreh
        if need <= value:
            return moreh
        moreh += 1


def get_height(heights, M):
    if len(heights) == 1:
        return heights[0] - M

    earns = [0]
    for i in range(1, len(heights)):
        dh = heights[i-1] - heights[i]
        v = i*dh + earns[i-1]
        if v == M:
            return heights[i]
        if v > M:
            return heights[i-1] - get_more_height(M-earns[i-1], i)
        earns.append(v)
    

    need = M-earns[-1]
    return heights[-1] - get_more_height(need, len(heights))

print(get_height(heights, M))
