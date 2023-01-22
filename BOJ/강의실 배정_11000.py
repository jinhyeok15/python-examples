import sys, bisect
input = sys.stdin.readline

N = int(input())

classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort()

rooms = [classes.pop(0)[1]]
for ct in classes:
    t = rooms[0]
    if ct[0] >= t:
        rooms.pop(0)
    bisect.insort(rooms, ct[1])
print(len(rooms))
