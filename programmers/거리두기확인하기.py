def dfs(data, start, place, visited, path, walk=0):
    if start != path and place[path[0]][path[1]] == 'P':
        data.append(walk)
        return

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for i in range(4):
        y, x = path
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue
        if place[ny][nx] == 'X': continue
        if visited[ny][nx]: continue
        
        visited[ny][nx] = True
        dfs(data, start, place, visited, (ny, nx), walk+1)
        visited[ny][nx] = False


def solution(places):
    answer = [None for _ in range(5)]
    
    for i, place in enumerate(places):
        visited = [[False for _ in range(5)] for _ in range(5)]
        for y in range(5):
            if answer[i] is not None: break
            
            for x in range(5):
                if answer[i] is not None: break
                
                if place[y][x] == 'P' and not visited[y][x]:
                    start = (y, x)
                    visited[y][x] = True
                    data = []
                    dfs(data, start, place, visited, path=start)

                    for m in data:
                        if m <= 2:
                            answer[i] = 0; break
        if answer[i] is None:
            answer[i] = 1
    return answer