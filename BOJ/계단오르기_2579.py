N = int(input())
stairs = [int(input()) for _ in range(N)]


class LookUp:
    def __init__(self,
        current: int,
        score: int,
        accum: int,
        strike: int
    ):
        self.current = current
        self.score = score
        self.accum = accum
        self.strike = strike


def bfs(start, stairs):
    q = []
    q.append(LookUp(start, stairs[start], stairs[start], 1))

    max_score = 0

    while q:
        lookup: LookUp = q.pop(0)

        if lookup.current == len(stairs)-1:
            max_score = max([lookup.accum, max_score])
            continue

        plans = next_plans(lookup, stairs)
        for plan in plans:
            q.append(plan)
    
    return max_score


def next_plans(lookup: LookUp, stairs):
    plans = []

    top = len(stairs)-1
    if lookup.current == top:
        return plans

    if lookup.strike + 1 != 3:
        idx = lookup.current + 1
        plans.append(
            LookUp(idx, stairs[idx], lookup.accum + stairs[idx], lookup.strike + 1)
        )
    
    if lookup.current + 2 > top:
        return plans

    idx = lookup.current + 2
    plans.append(
        LookUp(idx, stairs[idx], lookup.accum + stairs[idx], 1)
    )

    return plans


if N == 1:
    print(bfs(0, stairs))
else:
    print(max([bfs(0, stairs), bfs(1, stairs)]))

# N = 6
# stairs = [10, 20, 15, 25, 10, 20]
