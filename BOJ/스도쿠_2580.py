graph = []
questions = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

for y in range(9):
    for x in range(9):
        if graph[y][x] == 0:
            questions.append((y, x))


def dfs(curr=0):
    if curr >= len(questions):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for num in range(1, 10):
        y, x = questions[curr]
        if exist_cross((y, x), num) or exist_room((y, x), num):
            continue

        graph[y][x] = num
        dfs(curr+1)
        graph[y][x] = 0


def exist_cross(path, num):
    y, x = path
    for i in range(9):
        if graph[y][i] == num or graph[i][x] == num:
            return True
    return False


def exist_room(path, num):
    y, x = path
    for dy in range(3):
        for dx in range(3):
            if graph[y-y%3+dy][x-x%3+dx] == num:
                return True
    return False

dfs()
