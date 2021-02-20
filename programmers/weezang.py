
import collections

def solution(clothes:list)->int:

    answer:int
    sum:int = 1

    cloth_hash = collections.defaultdict(list)

    for cloth in clothes:
        cloth_hash[cloth[1]].append(cloth[0])

    #keys , values, items
    for kind in cloth_hash.values():
        #print(kind)
        sum *= (len(kind) + 1)
    answer = sum - 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))