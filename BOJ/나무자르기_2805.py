"""
나무 높이를 정렬한 후,
각각의 나무 높이 마다 얻을 수 있는 나무 개수를 list에 담고
M 이상을 얻을 수 있는 나무 높이 idx - 1 인 나무 높이에서 추가로 잘라야할 높이를 빼서 구한다.

나무 높이의 최댓값 maxH까지를 이진 탐색으로 탐색할 경우 O(log(maxH))의 시간 복잡도가 소요되는데,
log(maxH) * N 인 시간 복잡도와 비교했을 때,
나무 높이 증분을 dh라 하면
위의 풀이에서는 O(Nlog(N)) + O(dh)이 소요되는데 dh는 N의 길이가 커질 수록 작아지는 경향이 있기에
N의 길이가 크다면 위의 풀이가 압도적으로 빠르지 않을까?

또한 위의 풀이의 단점이 dh가 클 경우인데, 사실상 dh가 커지면 위의 이진 탐색 풀이도 시간복잡도를 장담할 수 없음...
왜냐하면 maxH는 dh보다 크기 때문
"""

N, M = map(int, input().split())
heights = sorted([int(s) for s in input().split()], reverse=True)


def get_more_height(need, target_tree):
    moreh = 0
    while True:
        value = target_tree * moreh
        if need <= value:
            return moreh
        moreh += 1


def get_height(heights, M):
    if len(heights) == 1:
        return heights[0] - M

    earns = [0]
    for i in range(1, len(heights)):
        dh = heights[i-1] - heights[i]
        v = i*dh + earns[i-1]
        if v == M:
            return heights[i]
        if v > M:
            return heights[i-1] - get_more_height(M-earns[i-1], i)
        earns.append(v)
    

    need = M-earns[-1]
    return heights[-1] - get_more_height(need, len(heights))

print(get_height(heights, M))
