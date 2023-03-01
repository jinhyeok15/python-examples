def solution(words, queries):
    answer = []
    comp = [[] for _ in range(10001)]
    for word in words:
        comp[len(word)].append(word) #왼쪽에서부터 비교할 문자열 계수정렬

    for query in queries:
        scope = (0, 0)
        length = len(query)
        cnt = 0
        lo = 0
        hi = length
        while lo < hi:
            mid = (lo+hi)//2
            if query[0] == '?':
                if query[mid] != '?': hi = mid
                else: lo = mid+1
            else:
                if query[mid] != '?': lo = mid+1
                else: hi = mid
        idx = lo
        scope = (idx, length) if query[0] == '?' else (0, idx)
        key = query[scope[0]:scope[1]]
        for word in comp[length]:
            if is_keyword(word, scope, key):
                cnt += 1
        answer.append(cnt)
    return answer


def is_keyword(word, scope, key):
    if word[scope[0]:scope[1]] == key:
        return True
    return False


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
