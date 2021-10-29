# from collections import defaultdict

# def solution(N, K):

#     answer_hash = defaultdict(int)


#     div, last = N, 0
#     count = 0
#     answer = 0

#     if N <= K: 
#         print(answer)
#         return 

#     while div != 1:
#         div, last = divmod(div, 2)
#         if last == 1: 
#             answer_hash[2 ** count] = 1
#         count += 1

#     answer_hash[2 ** count] = 1
#     answer_keys = list(answer_hash.keys())

#     now = answer_keys[0]

#     while now < answer_keys[-K]:
#         if answer_hash[now] == 1:
#             answer += now
#             answer_hash[now] += 1
#         if answer_hash[now] == 2:
#             answer_hash[now] = 0
#             answer_hash[now * 2] += 1
#         now *= 2


#     print(answer)

    
def solution(N, K):
    answer = 0

    while format(N, 'b').count('1') > K:
        temp = 2 ** format(N, 'b')[::-1].index('1')
        answer += temp 
        N += temp

    print(answer)







N, K = map(int, input().split())
solution(N, K)

 