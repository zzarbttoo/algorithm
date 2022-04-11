from collections import defaultdict

def solution():
    N = int(input())
    C = []

    for _ in range(N):
        C.append(int(input()))
    
    memo = defaultdict(lambda : 1)

    for i in range(N):
        for j in range(i):
            if C[i] > C[j]:
                if memo[i] < memo[j] + 1:
                    memo[i] = memo[j] + 1

    print(N - max(memo.values()))
    

solution()