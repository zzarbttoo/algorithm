from sys import stdin

def input_():
    n, k = map(int, stdin.readline().split())
    V = []

    for _ in range(n):
        V.append(int(stdin.readline()))
    return n, k, V

from collections import defaultdict

def solution():
    #n, k, V = input_()
    n, k = 3, 15
    V = [1, 5, 12]

    memo = defaultdict(lambda : float('INF'))
    memo[0] = 0

    for v in V:
        for i in range(v, k + 1):
            memo[i] = min(memo[i], memo[i - v] + 1)

    if memo[k] != float('INF'):
        print(memo[k])
    else:
        print(-1)

solution()
