from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    tree_length = 0

    for i in tree:
        if mid <= i:
            tree_length += i - mid
    
    if tree_length >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
