from collections import defaultdict

def solution(N, stages):

    num = defaultdict(int) #현재 스테이지에 머물러있는 사람
    add_num = defaultdict(int) 
    people_num = len(stages)

    before_sum = 0
    failure = defaultdict(float)

    for stage in stages:
        num[stage] += 1

    for i in range(1, N + 1):
        challenger = people_num - before_sum

        if challenger == 0: failure[i] = 0
        else: failure[i] = num[i] / challenger

        before_sum += num[i]

    return sorted(failure.keys(), key = lambda x : failure[x], reverse = True)