import math


def f(A):
    _sum = 0
    for i in range(math.sqrt(A)):
        num = i+1
        if A % num == 0:
            _sum += A / num
    return _sum


def g(N):
    m = [0 for _ in range(N+1)]

    if m[N]:
        return m[N]
    
