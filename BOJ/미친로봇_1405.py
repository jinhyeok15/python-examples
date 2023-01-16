_input_list = list(map(int, input().split(' ')))
N = _input_list[0]
percentages = _input_list[1:]


class Accumulation:
    def __init__(self):
        self.value = 0


def dfs(accumulation, current=(0, 0), visited=["0 0"], count=0, p=1.):
    if count == N:
        accumulation.value += p
        return
    x, y = current
    pathes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, path in enumerate(pathes):
        if percentages[i] == 0:
            continue
        moved = (x+path[0], y+path[1])
        if f"{moved[0]} {moved[1]}" in visited:
            continue
        visited.append(f"{moved[0]} {moved[1]}")
        dfs(accumulation, moved, visited, count+1, p*percentages[i]*0.01)
        visited.pop()

accumulation = Accumulation()
dfs(accumulation)
print(accumulation.value)
