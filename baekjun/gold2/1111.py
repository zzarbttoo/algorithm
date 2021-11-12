# from collections import Counter

# def solution(N, iq_list):
#     if N == 1:
#         return 'A'
#     iq_count = len(Counter(iq_list).keys())
#     if N == 2:
#         if iq_list[0] != iq_list[1]:
#             return 'A'
#         else:
#             if iq_count >= 2:
#                 return 'B'
#             else:
#                 return iq_list[0]

#     if iq_list[1] == iq_list[0]:
#         if iq_count >= 2:
#             return 'B'
#         return 'A'

#     a = (iq_list[2] - iq_list[1]) / (iq_list[1] - iq_list[0])
#     b = iq_list[1] - iq_list[0] * a

#     if a != int(a) or b != int(b):
#         return 'B'

#     for idx in range(1, N - 2):

#         if iq_list[idx + 1] == iq_list[idx]:
#             if iq_count >= 2:
#                 return 'B'
#             return 'A'
#         temp_a = (iq_list[idx + 2] - iq_list[idx + 1]) / (iq_list[idx + 1] - iq_list[idx]) 
#         temp_b= (iq_list[idx + 1] - iq_list[idx] * temp_a)

#         if temp_a != a or temp_b != b:
#             return 'B'
    
#     return int(a * iq_list[-1] + b)



N = int(input())
iq = list(map(int, input().split()))
print(solution(N, iq))