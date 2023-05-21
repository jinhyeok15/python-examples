def solution(cap, n, deliveries, pickups):
    dist = 0
    d_remain, p_remain = 0, 0
    for i in reversed(range(n)):
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        while d_remain > 0 or p_remain > 0:
            d_remain -= cap
            p_remain -= cap
            dist += 2 * (i+1)
    return dist
