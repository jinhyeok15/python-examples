class Hurdle:
    def __init__(self, height: int, direction: int, H: int):
        self.height = height
        self.direction = direction

        if direction == -1:
            self.range = (H-self.height, H-1)
        else:
            self.range = (0, self.height-1)


N, H = tuple(map(int, input().split(" ")))
hurdles = []
for i in range(N):
    hurdle = Hurdle(int(input()), 1 if i%2==0 else -1, H)
    hurdles.append(hurdle)

minimum = N
same_level = 0
for i in range(H):
    cnt = 0
    is_valid = True
    for hurdle in hurdles:
        if hurdle.range[0] <= i and hurdle.range[1] >= i:
            cnt += 1
            if cnt > minimum:
                is_valid = False
                break
    if is_valid:
        if minimum == cnt:
            same_level += 1
        elif minimum > cnt:
            same_level = 1
            minimum = cnt


print(f"{minimum} {same_level}")
