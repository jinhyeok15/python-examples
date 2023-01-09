def solution(n, times):
    answer = 0

    lo = min(times)
    hi = max(times) * n

    while lo < hi:
        mid = (lo + hi) // 2
        if bigger_than_mid(n, mid, times):
            lo = mid + 1
        else:
            hi = mid
    answer = lo
    return answer


def bigger_than_mid(n, mid, times):
    cnt = 0
    for time in times:
        cnt += mid // time
    if cnt >= n:
        return False
    return True
