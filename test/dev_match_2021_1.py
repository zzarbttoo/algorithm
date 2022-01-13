from collections import defaultdict

def solution(lottos, win_nums):

    order = defaultdict(int)
    count = defaultdict(int)

    for i in range(1, 7):
        order[i] = 7 - i
    order[0] = 6

    for lo in lottos:
        count[lo] += 1
    min, max = 0, 0

    for win in win_nums:
        if count[win] != 0:
            min += 1
    max += min+ count[0]
    return [order[max], order[min]]

    # def solution(lottos, win_nums):

    # rank=[6,6,5,4,3,2,1]

    # cnt_0 = lottos.count(0) 
    # ans = 0
    # for x in win_nums:
    #     if x in lottos:
    #         ans += 1
    # return rank[cnt_0 + ans],rank[ans]

    # def solution(lottos, win_nums):
    # rank = {
    #     0: 6,
    #     1: 6,
    #     2: 5,
    #     3: 4,
    #     4: 3,
    #     5: 2,
    #     6: 1
    # }
    # return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]