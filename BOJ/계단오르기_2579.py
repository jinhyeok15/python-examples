N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

m = []

if N <= 2:
    print(sum(stairs))
else:
    m.append(stairs[0])
    m.append(stairs[0]+stairs[1])
    m.append(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
    for i in range(3, N):
        m.append(max(m[i-3]+stairs[i-1]+stairs[i], m[i-2]+stairs[i]))
    print(m[-1])
