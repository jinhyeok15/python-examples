def solution(user_id, banned_id):
    visited = [[False] * len(user_id) for _ in range(len(banned_id))]
    listed = [[] for _ in range(len(banned_id))]
    for i, q in enumerate(banned_id):
        for j, u in enumerate(user_id):
            size = len(q)
            if len(u) != size or visited[i][j]:
                continue
            for k in range(size):
                if q[k] == '*' or u[k] == q[k]:
                    continue
                visited[i][j] = True
                break
            if not visited[i][j]:
                listed[i].append(u)
    visited = set()
    answer_set = set()
    def dfs(cur=0):
        if cur >= len(listed):
            answer_set.add(frozenset(visited.copy()))
            return
        for user in listed[cur]:
            if user not in visited:
                visited.add(user)
                dfs(cur+1)
                visited.remove(user)
    dfs()
    return len(answer_set)
