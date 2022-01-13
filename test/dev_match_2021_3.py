from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):

    parent = defaultdict(str)
    money = defaultdict(float)

    for en, ref in zip(enroll, referral):
        parent[en] = ref

    for sel, am in zip(seller, amount):
        temp = defaultdict(float)
        temp[sel] = am * 100


        while parent[sel] != "":
            ten_p = math.floor(temp[sel] / 10)
            if ten_p < 1: break
            temp[parent[sel]] = ten_p
            temp[sel] = temp[sel] - temp[parent[sel]]
            sel = parent[sel] 

        for key, val in temp.items():
            money[key] += val

    result = []

    for en in enroll:
        result.append(money[en])

    return result