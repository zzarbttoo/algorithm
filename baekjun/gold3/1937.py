import sys
sys.setrecursionlimit(10**6)

def input_():
    n = int(sys.stdin.readline())
    T = []

    for _ in range(n):
        T.append(list(map(int, sys.stdin.readline().split())))
    
    return n, T

from collections import defaultdict 

def solution():
    n, T = input_()
    answer = 0
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    m = defaultdict(lambda : defaultdict(lambda : -1))

    def dfs(y, x):
        nonlocal m, n, T, direction
        if m[y][x] == -1: 
            m[y][x] = 0

            for d in direction:
                dy, dx = y + d[0], x + d[1]
                if 0 <= dy < n and 0 <= dx < n and T[dy][dx] < T[y][x]:
                    m[y][x] = max(m[y][x], dfs(dy, dx))
        
        return m[y][x] + 1
            

    for y in range(n):
        for x in range(n):
            answer = max(answer, dfs(y, x))

    print(answer)

solution()

