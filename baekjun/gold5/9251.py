from collections import defaultdict

def solution():

    A = input()
    B = input()

    cnt = defaultdict(lambda : defaultdict(int))

    for b in range(len(B)):
        for a in range(len(A)):
            if B[b] == A[a]: cnt[b][a] += cnt[b - 1][a - 1] + 1
            else: cnt[b][a] = max(cnt[b - 1][a], cnt[b][a - 1])
    
    print(cnt[len(B) - 1][len(A) - 1])

solution()

