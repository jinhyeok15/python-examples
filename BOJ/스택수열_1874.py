def _push(cur, stack, record):
    stack.append(cur)
    record.append('+')


def _pop(stack, record):
    v = stack.pop()
    record.append('-')
    return v

n = int(input())
sequence = [int(input()) for _ in range(n)]
answer = None

stack = []
record = []

cur = 0
for num in sequence:
    if stack:
        if num == stack[-1]:
            _pop(stack, record)
            continue

    while cur < num:
        cur += 1
        _push(cur, stack, record)

    if cur == num:
        _pop(stack, record)

if stack: print('NO')
else:
    for r in record: print(r)
