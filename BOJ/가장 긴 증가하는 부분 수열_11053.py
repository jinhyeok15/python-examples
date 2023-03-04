from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]

dp = [A[0]]

for i in range(N):
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp))
