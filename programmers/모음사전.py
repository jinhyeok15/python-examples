from bisect import bisect

def solution(word):
    max_length = 5
    pools = [('A', 'E', 'I', 'O', 'U')] * max_length
    result = [[]]
    words = []
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
        for i in result:
            words.append(''.join(i))
    dictionary = sorted(words)
    return bisect(dictionary, word, 0)
