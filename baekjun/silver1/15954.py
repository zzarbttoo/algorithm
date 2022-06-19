
from collections import defaultdict

def solution():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    s = 0
    s_m = defaultdict(int)

    for i, d in enumerate(D):
        s += d
        s_m[i] = s

    for i in range(N):
        print("i :::: " + str(i))
        for j in range(i + K - 1, N):
            n = j - i + 1
            print(n)
            




solution()