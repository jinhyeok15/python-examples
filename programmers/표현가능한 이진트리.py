def binsearch(binstr, status):
    _length = len(binstr)
    if _length == 1 or len(set(binstr)) == 1:
        return

    mid = _length // 2
    if binstr[mid] == '0':
        status[0] = 0
        return

    binsearch(binstr[:mid], status)
    binsearch(binstr[mid+1:], status)


def solution(numbers):
    answer = []
    bin_list = [2**x - 1 for x in range(50)]

    for num in numbers:
        binstr = format(num, 'b')
        _length = len(binstr)
        for size in bin_list :
            if size >= _length :
                binstr = '0'*(size-_length) + binstr
                break
        status = [1]
        binsearch(binstr, status)
        answer += status
    return answer
