import heapq


def solution(N, stages):
    get_failure = lambda x, y: x / y if y != 0 else 0
    counted = [0] * (N+2)
    accu = 0
    for stage in stages:
        counted[stage] += 1
        accu += 1
    failure_info = []
    for i in range(1, N+1):
        heapq.heappush(failure_info, (-get_failure(counted[i], accu), i))
        accu -= counted[i]
    answer = []
    while failure_info:
        answer.append(heapq.heappop(failure_info)[1])
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
