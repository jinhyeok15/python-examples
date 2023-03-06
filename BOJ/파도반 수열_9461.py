T = int(input())
for i in range(T):
    dp = [0] * 101
    N = int(input())
    dp[1], dp[2], dp[3] = 1, 1, 1
    if N <= 3:
        print(dp[N])
    else:
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[N])
