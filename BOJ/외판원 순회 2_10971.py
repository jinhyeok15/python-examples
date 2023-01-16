N = int(input())

costs = []
for i in range(N):
    costs.append(list(map(int, input().split(' '))))


class MinCost:
    def __init__(self, N, costs):
        self.value = None
        self.costs = costs
        self.size = N
    
    def _set(self, cost):
        if self.value is None:
            self.value = cost
            return
        self.value = min(cost, self.value)
    
    def _dfs(self, start, visited, current_cost=0):
        if len(visited) == self.size:
            cost = self.costs[start][visited[0]]
            if cost == 0: return
            current_cost += cost
            self._set(current_cost)
            return
        if self.value is not None and current_cost > self.value:
            return

        for end in range(self.size):
            cost = self.costs[start][end]
            if cost == 0: continue
            if end in visited:
                continue
            visited.append(end)
            self._dfs(end, visited, current_cost + cost)
            visited.pop()

    def run(self):
        for i in range(self.size):
            self._dfs(i, [i])


def solution(N, costs):
    min_cost = MinCost(N, costs)
    min_cost.run()
    return min_cost.value


if __name__ == "__main__":
    print(solution(N, costs))
