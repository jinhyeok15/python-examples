from functools import reduce
from itertools import permutations


sentence = input()
words = reduce(
    lambda acc, _: [*acc, input()],
    range(int(input())),
    []
)

sentence_copy = sentence

result_cnt = 0

for word in words:
    exchanged_word_list = list(set(permutations(list(word))))

    min_applied_cnt, applied_sentence = 0, sentence_copy
    for partition in exchanged_word_list:
        exchanged_word = ''.join(partition)
        
        _sentence = applied_sentence.replace(exchanged_word, '')
        if applied_sentence != _sentence:
            _cnt = reduce(
                lambda acc, cur: acc+1 if word[cur] != exchanged_word[cur] else acc,
                range(len(word)),
                0
            )
            
            compared = min_applied_cnt if min_applied_cnt else _cnt
            
            if _cnt <= compared:
                min_applied_cnt, applied_sentence = _cnt, _sentence
    
    result_cnt += min_applied_cnt
    sentence_copy = applied_sentence

if sentence_copy:
    print(-1)
else:
    print(result_cnt)
