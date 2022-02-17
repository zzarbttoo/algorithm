import enum
from sys import stdin

def input_():
    n = int(stdin.readline())
    L = []
    for _ in range(n):
        L.append(list(map(int, stdin.readline().split())))

    return n, L

from collections import defaultdict

def solution():
    #n, L = input_()
    n, L = 8, [[1, 8], [3, 9], [2, 2], [4, 1], [6, 4], [10, 10], [9, 7], [7, 6]]

    memo = defaultdict(int)
    L.sort(key = lambda x: x[0])

    for i, l in enumerate(L):
        print("L ::: " + str(l))
        for j in range(0, i):
            if L[j][1] > l[1] and memo[i] < memo[j]: # 전에 꺼가 더 크고 현재 꺼가 memo가 더 클 경우
                memo[i] = memo[j]
        memo[i] += 1
    
    print(n - max(memo.values()))
    









solution()