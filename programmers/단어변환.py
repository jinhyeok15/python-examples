from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()

    def _bfs(words, node, count=0):
        queue.append((node, count))

        while queue:
            key, depth = queue.popleft()
            for neighbor in words:
                if is_exchangable(key, neighbor):
                    if neighbor == target:
                        return depth+1
                    queue.append((neighbor, depth+1))
        
    return _bfs(words, begin)


def is_exchangable(begin, word):
    cnt = 0
    for i in range(len(begin)):
        if cnt > 1:
            return False
        if begin[i] != word[i]:
            cnt += 1
    return cnt == 1


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
