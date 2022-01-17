# from itertools import combinations


# def solution():
#     S, K= map(int, input().split())

#     iter = [i for i in range(1, S + 1)]
#     answer = -float('INF')

      #중복 허용 안하는 줄 깔깔
#     for nums in list(combinations(iter, K)):
#         temp = 1
#         if sum(nums) == S:
#             print(nums)
#             for n in nums:
#                 temp *= n
#             if temp > answer:
#                 answer = temp


#     print(answer)




def solution():
    S, K= map(int, input().split())

    li = [S//K for _ in range(K)]
    for idx in range(S % K): li[idx] += 1
    answer = 1
    for l in li:
        answer *= l
    
    print(answer)



solution()
