if __name__ == "__main__":
    channel = input()

    available_channel = '100'

    result = abs(int(channel)-int(available_channel))
    
    M = int(input())
    if M:
        unwork_btns = input().split(' ')

    if len(channel) >= result:
        print(result)
    elif M==10:
        print(result)
    elif M:
        # left
        _left_ch = channel
        _left_result = len(channel) if int(channel) else int(available_channel)
        while int(_left_ch) > 0:
            _flag = False
            for btn in unwork_btns:
                if btn in _left_ch:
                    _flag = True
                    break
            if _flag:
                _left_ch = str(int(_left_ch)-1)
                _left_result = int(channel) - int(_left_ch) + len(_left_ch)
                if not int(_left_ch):
                    for btn in unwork_btns:
                        if btn in _left_ch:
                            _left_result = 100000
            else:
                break

        # right
        _right_ch = channel
        _right_result = len(channel)
        while _right_result < _left_result:
            _flag = False
            for btn in unwork_btns:
                if btn in _right_ch:
                    _flag = True
                    break
            if _flag:
                _right_ch = str(int(_right_ch)+1)
                _right_result = int(_right_ch) - int(channel) + len(_right_ch)
            else:
                break
        result = min(_left_result, _right_result, result)
        print(result)
    else:
        result = len(channel)
        print(result)
