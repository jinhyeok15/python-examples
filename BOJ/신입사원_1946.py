import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cand = [[int(i) for i in input().split()] for _ in range(N)]
    cand.sort()
    second_min = cand[0][1]
    cnt = 1
    for i in range(1, N):
        a = cand[i]
        if a[1] < second_min:
            cnt += 1
            if a[1] == 1: break
            second_min = a[1]
    print(cnt)
