left_braces = ['(', '[']
right_braces = [')', ']']

pairs = zip(left_braces, right_braces)

s = input()

def brace_value(string):
    brace_stack = []
    tmp = [1]

    for c in string:
        if c in left_braces:
            brace_stack.append(c)
        elif c in right_braces:
            if brace_stack:
                left = brace_stack.pop()
                right = c
                if (left, right) not in pairs:
                    return 0
                if (left, right) == ('(', ')'):
                    tmp[-1] *= 2
                else:
                    tmp[-1] *= 3
                if not brace_stack:
                    tmp.append(1)
            else: return 0
        else: return 0
    return sum(tmp)

print(brace_value(s))
