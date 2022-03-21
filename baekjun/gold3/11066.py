def solution():
    N = int(input())
    answer = []
    for _ in range(N):
        answer.append(program())
    
    for a in answer:
        print(a)

from collections import defaultdict

def program():
    K = int(input())
    F = list(map(int, input().split()))

    me = defaultdict(lambda : defaultdict(lambda : float('INF')))
    sum = defaultdict(int)

    for i in range(K):
        me[i][i] = 0
        sum[i] = sum[i - 1] + F[i]
        if i != K - 1: me[i][i + 1] = F[i] + F[i + 1]
    
    for k in range(3, K + 1): #길이
        for i in range(K - (k - 1)): #시작점
            me[i][k + i - 1]= min([me[i][j] + me[j + 1][i + k - 1] for j in range(i, i + k - 1)]) + sum[k + i - 1] - sum[i - 1]

    return me[0][K - 1]

solution()

