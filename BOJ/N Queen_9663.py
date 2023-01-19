N = int(input())
ans = 0
board = [0] * N


def dfs(idx=0):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        board[idx] = i
        if not is_attacked(idx, board):
            dfs(idx+1)


def is_attacked(idx, board):
    for i in range(idx):
        if board[i] == board[idx] or abs(board[i]-board[idx]) == abs(i-idx):
            return True
    return False


dfs()
print(ans)
