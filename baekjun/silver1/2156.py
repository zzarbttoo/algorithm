from collections import defaultdict

def solution():
    n = int(input())
    G = []
    for _ in range(n):
        G.append(int(input()))
    
    memo = defaultdict(int)

    if n == 1:
        return G[0]
    
    if n == 2:
        return G[0] + G[1]

    memo[0], memo[1] = G[0], memo[0] + G[1]

    for i in range(1, n):
        memo[i] = max(memo[i - 1], memo[i - 3] + G[i - 1] + G[i], memo[i - 2] + G[i])

    return memo[n - 1]


print(solution())
