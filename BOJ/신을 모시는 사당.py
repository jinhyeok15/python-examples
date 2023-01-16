import sys
sys.setrecursionlimit(100000)

def earn(mem, size, num, N, dolsang):
    golds = dolsang[num-1:num-1+size]
    if size == N:
        left = golds.count(1)
        mem[size-1] = abs(2*left - N)
        return

    if num + size > N:
        return
    
    if mem[size-1] is not None:
        value = mem[size-1] - dolsang[num-1] if dolsang[num-1] == 1 else -1 + dolsang[num+size-1] if dolsang[num+size-1] == 1 else -1
        mem[size-1] = max([abs(value), mem[size-1]])
    else:
        left = golds.count(1)
        mem[size-1] = abs(2*left - N)
    earn(mem, size, num+1, N, dolsang)


N = int(sys.stdin.readline())
dolsang = list(map(int, sys.stdin.readline().split(' ')))

mem = []
for i in range(1, N+1):
    mem.append(None)
    earn(mem, i, 1, N, dolsang)
print(max(mem))
