from sys import stdin

def input_():

    N, M = map(int, stdin.readline().split())
    R = []
    
    for _ in range(N):
        R.append(stdin.readline().strip())

    return N, M, R

        
from collections import deque
from collections import defaultdict

def solution():
    N, M, R = input_()

    q = deque([])
    visited = defaultdict(lambda : defaultdict(bool))

    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]   
    q.append([0, 0, 1])

    while q:
        t = q.popleft()
        y, x, c = t[0], t[1], t[2]

        if y >= (N - 1) and x >= (M - 1):
            print(c)
            return 

        for d in direction:
            ny , nx = y + d[0], x + d[1]
            if 0 <= ny < N and 0 <= nx < M:
                if R[ny][nx] == '1' and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append([ny, nx, c + 1])


solution()