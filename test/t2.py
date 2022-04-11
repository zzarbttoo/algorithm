from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

def solution():
    N, Q = map(int, input().split())
    A = list(input().split()) #값은 A[N - 1]
    R = defaultdict(list)
    P = []

    for _ in range(N - 1):
        t = list(map(int, input().split()))
        R[t[0]].append(t[1])
        R[t[1]].append(t[0])

    for _ in range(Q):
        P.append(list(map(int, input().split())))

    visited = defaultdict(bool)
    nums = []

    def dfs(end, now):
        nonlocal visited, nums, A, R

        for r in R[now]:
            if visited[r]: continue
            visited[r] = True
            nums.append(A[r - 1])
            if end == r:
                print(int(''.join(nums)) % 1000000007)
            else:
                dfs(end, r)
            visited[r] = False
            nums.pop()

    for p in P:
        if p[0] == p[1]:
            print(int(A[p[0] - 1]) % 1000000007)
            continue
        visited[p[0]] = True
        nums.append(A[p[0] - 1]) 
        dfs(p[1], p[0])
        visited[p[0]] = False
        nums.pop()


solution()