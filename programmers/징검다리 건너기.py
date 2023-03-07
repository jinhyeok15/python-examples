def solution(stones, k):
    lo = min(stones)
    hi = max(stones)
    
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = 0
        for stone in stones:
            if cnt >= k:
                break
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0
        if cnt < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
