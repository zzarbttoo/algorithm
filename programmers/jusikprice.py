'''
import collections
def solution(prices:list)->list:

    hash = collections.defaultdict(int)
    stack = []

    for i, price in enumerate(prices):

        if prices[i-1] and  prices[i-1] > prices[i] and stack:
            temp=stack.pop()
            stack.append([price, i]) 
        else:
            stack.append([price, i])

        


    return []
'''

from collections import deque 
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        # stack을 사용하지 않고 그냥 일일히 셈
        for i in prices:
            if c > i:
                count += 1
                break 
            count += 1

        answer.append(count)

    return answer

def solution1(prices:list)->list:
    #hash 로 하지 않고 이러는 것이 더 편할 듯
    answer = [0] * len(prices)
 
    for i in range(len(prices)):
        # push 된 다음 수들만 체크
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer



print(solution([1, 2, 3, 2, 3]))
print(solution1([1, 2, 3, 2, 3]))

