from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    total = q1_sum + q2_sum
    if total % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while True:
        if answer >= 2*(len(queue1) + len(queue2)):
            return -1
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            v = queue1.popleft()
            q1_sum -= v
            queue2.append(v)
            q2_sum += v
        else:
            v = queue2.popleft()
            q2_sum -= v
            queue1.append(v)
            q1_sum += v
        answer += 1
    return answer
