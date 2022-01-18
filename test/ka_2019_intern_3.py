

#시간 초과
from collections import defaultdict

def solution(gems):
    
    answer = [-1, 1000001]
    l, r = 0, 0
    
    a = defaultdict(int)
    for gem in gems: a[gem] += 1
    all = list(a.keys())
    
    k = defaultdict(int)
    k[gems[0]] += 1
    
    while l < len(gems) + 1 and r < len(gems) + 1 and l <= r:
        t = 1
        for n in all:
            t *= k[n]
        if t != 0:
            if answer[1] - answer[0] > r - l:
                answer = [l, r]
            if l < len(gems): k[gems[l]] -= 1
            l += 1
        else:
            r += 1
            if r < len(gems) : k[gems[r]] += 1
    
    answer[0] += 1
    answer[1] += 1
    return answer

# # from collections import defaultdict

# # def solution(gems):
    
# #     l = defaultdict(list)
# #     for idx, gem in enumerate(gems):
# #         l[gem].append(idx)
    
# #     leng = len(l.keys())
    
# #     while leng < len(gems):
# #         #start
# #         for start in range(0, len(gems) - leng + 1, 1):
# #             c = defaultdict(int)
# #             t_a = 1
# #             for atom in range(start, start + leng):
# #                 c[gems[atom]] += 1
# #             for k in l.keys():
# #                 t_a *= c[k]
# #             if t_a != 0:
# #                 return [start + 1, start + leng]

# #         leng += 1
# #     return [1, len(gems)]


# #시간 초과 
# from collections import defaultdict

# def solution(gems):
#     answer = []
    
#     l, r = 0, 0
#     gem_h = defaultdict(int)
    
#     for gem in gems:
#         gem_h[gem] += 1
#     all = list(gem_h.keys())
    
#     answer = [-1, 1000001] #최대
    
#     while(l < len(gems) + 1 and r < len(gems) + 1):
#         c = defaultdict(int)
#         for i in range(l, r):
#             c[gems[i]] += 1
#         if len(c.keys()) < len(all):
#             r += 1
#         else:
#             if answer[1] - answer[0] > r - l:
#                 answer = [l, r]
#             l += 1
#     answer[0] += 1
#     return answer 


