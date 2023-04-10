def solution(alp, cop, problems):
    cur_cost = 0
    
    max_needs = (0, 0)
    min_needs = (21, 21)
    for p in problems:
        max_needs = (max(max_needs[0], p[0]), max(max_needs[1], p[1]))
        min_needs = (min(min_needs[0], p[0]), min(min_needs[1], p[1]))

    if min_needs[0] > alp:
        cur_cost += min_needs[0] - alp
    if min_needs[1] > cop:
        cur_cost += min_needs[1] - cop
    
    dp = [[float('inf')] * max_needs[1] for _ in range(max_needs[0])]
    dp[min_needs[0]][min_needs[1]] = cur_cost
    
    for i in range(min_needs[0], max_needs[0]+1):
        for j in range(min_needs[1], max_needs[1]+1):
            if i < max_needs[0]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_needs[1]:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    _alp, _cop = min(i+alp_rwd, max_needs[0]), min(j+cop_rwd, max_needs[1])
                    dp[_alp][_cop] = min(dp[_alp][_cop], dp[i][j]+cost)

    return dp[max_needs[0]][max_needs[1]]
