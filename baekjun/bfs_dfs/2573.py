from sys import stdin
from collections import defaultdict

def input_():
    N, M = map(int, stdin.readline().split())
    W = []
    
    for _ in range(N):
        W.append(list(map(int, stdin.readline().split())))
    
    return N, M, W

from copy import deepcopy
from collections import deque

def solution():

    N, M, W = input_()
    # N, M , W = 5, 7, [
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 2, 4, 5, 3, 0, 0],
    #     [0, 3, 0, 2, 5, 2, 0],
    #     [0, 7, 6, 2, 4, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    # ]

    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def melt(W):
        nonlocal direction

        n_W = deepcopy(W)

        for y in range(N):
            for x in range(M):
                cnt = 0
                if W[y][x] != 0:
                    for d in direction:
                        ny, nx = y + d[0], x + d[1]
                        if 0 <= ny < N and 0 <= nx < M:
                            if W[ny][nx] == 0:
                                cnt += 1
                    n_W[y][x] -= cnt 
                    if n_W[y][x] <= 0: n_W[y][x] = 0

        return n_W

    def ct(W):

        nonlocal direction
        cnt = 0
        vi = defaultdict(lambda : defaultdict(bool))
        qu = deque([])

        for y in range(N):
            for x in range(M):
                if W[y][x] != 0 and vi[y][x] == False:
                    cnt += 1
                    qu.append([y, x])

                    while qu:
                        n = qu.popleft()
                        for d in direction:
                            ny, nx = n[0] + d[0], n[1] + d[1]
                            if 0 <= ny < N and 0 <= nx < M and vi[ny][nx] == False and W[ny][nx] != 0:
                                vi[ny][nx] = True
                                qu.append([ny, nx])
        
        return cnt 

    time = 0


    while True:

        if ct(W) >= 2: return time
        time += 1

        W = melt(W)

print(solution())