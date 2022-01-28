# def solution(prices):
    
#     answer = []
    
#     for idx, p in enumerate(prices):
#         count = 0
#         for num in prices[idx + 1:]:
#             count += 1
#             if num < prices[idx]:
#                 break
#         answer.append(count)
#     return answer

#매번 복사하는 것 보다 빠르다 
from collections import deque

def solution(prices):
    answer = []
    nums = deque(prices[:])
    
    for now in prices:
        nums.popleft()
        count = 0
        
        for ne in nums:
            count += 1
            if now > ne: break
        answer.append(count)
        
    return answer
