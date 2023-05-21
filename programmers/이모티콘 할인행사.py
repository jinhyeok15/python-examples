import heapq


def get_result(users, emoticons, method):
    subscriber = 0
    sails = 0
    
    for user in users:
        sum_ = 0
        flag = False
        for i, emo in enumerate(emoticons):
            per = method[i]
            dis_p = int(((100 - per) * emo / 100))
            if user[0] <= per:
                if sum_ + dis_p < user[1]:
                    sum_ += dis_p
                else:
                    subscriber += 1
                    flag = True
                    break
        if not flag:
            sails += sum_
    return subscriber, sails


def dfs(cur, users, emoticons, discounts, method, h):
    if cur >= len(emoticons):
        subscriber, sails = get_result(users, emoticons, method)
        heapq.heappush(h, (-subscriber, -sails))
        return
    
    for d in discounts:
        method.append(d)
        dfs(cur+1, users, emoticons, discounts, method, h)
        method.pop()


def solution(users, emoticons):
    h = []
    discounts = [10, 20, 30, 40]
    dfs(0, users, emoticons, discounts, [], h)
    v = heapq.heappop(h)
    return [-v[0], -v[1]]
