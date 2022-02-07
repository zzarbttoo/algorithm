from sys import stdin

def input_data():
    N, K = map(int, stdin.readline().split())
    W = []
    V = []

    for _ in range(N):
        w, v = map(int, stdin.readline().split())
        W.append(w)
        V.append(v)
    
    return N, K, W, V

from collections import defaultdict

def solution():
    N, K, W, V = input_data() #갯수, 최대 무게
    memo = defaultdict(lambda : defaultdict(int))

    for i in range(N): #N개 물건
        for k in range(1, K + 1): #1 ~ K kg
            if k < W[i]:
                memo[i][k] = memo[i - 1][k] 
            else:
                memo[i][k] = max(memo[i - 1][k], memo[i - 1][k - W[i]] + V[i])

    print(memo[N - 1][K])


solution()



# def solution():
#     N, K, WV = input_data()
#     #N, K, WV = 4, 7, [[6, 13], [4, 8], [3, 6], [5, 12]] 
#     memo = defaultdict(int)
#     memo[0] = 0

#     for wv in WV: #무게 -> 이득
#         temp = list(memo.keys())
#         for key in temp:
#             if key + wv[0] > 0:
#                 memo[key + wv[0]] = max(memo[key + wv[0]], memo[key] + wv[1])

#     answer = 0 
#     for i in range(K, 0, -1):
#         if memo[i] != 0: 
#             answer = memo[i]
#             break

#     print(answer)



# solution()
            












    




