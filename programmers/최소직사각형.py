def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        w = max(size) if w<max(size) else w
        h = min(size) if h<min(size) else h
    return w * h
