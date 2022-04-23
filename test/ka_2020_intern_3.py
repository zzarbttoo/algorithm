from collections import defaultdict
from collections import Counter

def solution(gems):
    
    count = Counter(gems).keys()
    w_cnt = len(count)
    
    start, end = 0, 0
    
    answer = [1, len(gems)] #전체 
    di = {}
    for i in range(start, end + 1):
        if not gems[i] in di:
            di[gems[i]] = 1
        else:
            di[gems[i]] += 1 
    
    while start <= end < len(gems):
        if len(di) == w_cnt:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]
            di[gems[start]] -= 1
            if di[gems[start]] == 0:
                word= gems[start]
                del di[word]
            start += 1
        else:
            end += 1 
            if end >= len(gems):
                break
            if not gems[end] in di:
                di[gems[end]] = 1 
            else:
                di[gems[end]] += 1
	
    return answer
# from collections import defaultdict
# from collections import Counter

# def solution(gems):
    
#     count = Counter(gems).keys()
#     w_cnt = len(count)
    
#     start, end = 0, 0
    
#     answer = [1, len(gems)] #전체 
    
#     while 0 <= start <= end < len(gems):
#         di = defaultdict(int)
#         for i in range(start, end + 1):
#             di[gems[i]] += 1
#         if len(di) == w_cnt:
#             if answer[1] - answer[0] > end - start:
#                 answer = [start + 1, end + 1]
#             start += 1
#         else:
#             end += 1
            
#     return answer
                