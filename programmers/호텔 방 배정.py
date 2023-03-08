import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    answer = []
    node = {}

    def search(n):
        if n not in node:
            node[n] = n+1
            return n
        else:
            tmp = search(node[n])
            node[n] = tmp + 1
            return tmp

    for n in room_number:
        allocated = search(n)
        answer.append(allocated)
    return answer
