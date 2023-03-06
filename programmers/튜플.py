def solution(s):
    answer = []
    comps = sorted([(len(i.split(',')), set(map(int,i.split(',')))) for i in s[2:len(s)-2].split("},{")])
    for c in comps:
        tmp = c[1]-set(answer)
        answer.append(tmp.pop())
    return answer
