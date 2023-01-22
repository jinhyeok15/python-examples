s = input()
splited_by_minus = s.split('-')

arr = []
for i, s in enumerate(splited_by_minus):
    _sum = sum(map(int, s.split("+")))
    if i==0:
        arr.append(_sum)
    else:
        arr.append(-1 * _sum)
print(sum(arr))
