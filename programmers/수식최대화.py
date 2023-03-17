from itertools import permutations


def solution(expression):
    answer = 0
    signlist = ['-', '*', '+']
    sign_length = len(signlist)
    
    digits = ''
    stack = []
    for s in expression:
        if s in signlist:
            stack += [int(digits), s]
            digits = ''
        else:
            digits += s
    stack.append(int(digits))

    for priority in permutations(signlist, sign_length):
        dp = [[] for _ in range(sign_length+1)]
        dp[0] = stack
        for idx in range(sign_length):
            plan = dp[idx]
            sign = priority[idx]
            flag = False
            for i in range(len(plan)):
                if plan[i] == sign:
                    preval = dp[idx+1][-1]
                    dp[idx+1][-1] = calculate(preval, plan[i+1], plan[i])
                    flag = True
                elif flag and isinstance(plan[i], int):
                    flag = False
                else:
                    dp[idx+1].append(plan[i])
        
        x = abs(dp[sign_length][0])
        if x > answer:
            answer = x
    return answer


def calculate(a, b, sign):
    if sign == '-':
        return a-b
    if sign == '+':
        return a+b
    if sign == '*':
        return a*b
