from re import L
from sys import stdin

def input_():
    N, M = map(int, stdin.readline().split())
    now = list(map(int, stdin.readline().split()))
    A = []

    for _ in range(N):
        A.append(list(map(int, stdin.readline().split())))
    
    return N, M, now, A


from collections import defaultdict

def solution():
    #N, M, now, A = input_()
    N, M, now = 3, 3, [1, 1, 0]
    A = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    vi = defaultdict(lambda : defaultdict(int))

    direction = {0 : [-1, 0], 1 : [0, 1], 2 : [1, 0], 3 : [0, -1]}
    rotation = {0 : 3, 3 : 2, 2 : 1, 1 : 0}

    


    dfs(now)




