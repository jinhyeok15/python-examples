def solution(numbers, hand):
    my_phone = Phone(hand)
    for num in numbers:
        my_phone.click(str(num))
    answer = ''.join(my_phone.data)
    return answer


class Phone:
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    
    def __init__(self, hand):
        self.L = (3, 0)
        self.R = (3, 2)
        self.hand = hand
        self.data = []
    
    def click(self, num: str) -> None:
        path = self._find_path(num)
        if num in ['1', '4', '7']:
            self.data.append('L')
            self.L = path
            return
        elif num in ['3', '6', '9']:
            self.data.append('R')
            self.R = path
            return
        near_hand = self._find_near_hand(path)
        if near_hand == 0:
            self.data.append('L')
            self.L = path
        else:
            self.data.append('R')
            self.R = path
    
    def _find_path(self, num):
        for i, row in enumerate(self.keypad):
            for j, key in enumerate(row):
                if key==num:
                    return (i, j)
        raise ValueError
    
    # 만약 오른손이 가까우면 1, 왼손이 가까우면 0
    def _find_near_hand(self, path):
        left_dist = abs(path[0]-self.L[0])+abs(path[1]-self.L[1])
        right_dist = abs(path[0]-self.R[0])+abs(path[1]-self.R[1])
        if left_dist == right_dist:
            return 1 if self.hand=='right' else 0
        return 1 if left_dist>right_dist else 0