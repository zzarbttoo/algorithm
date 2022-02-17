from sys import stdin 
import sys 
sys.setrecursionlimit(6000)

def input_():
    N = int(stdin.readline())
    H = []
    for _ in range(N):
        H.append(stdin.readline().strip())
    
    return N, H

from collections import defaultdict

def solution():
    N, H = input_()
    #N = 7
    #H = ['0110100', '0110101' , '1110101', '0000111', '0100000', '0111110', '0111000']
    memo = defaultdict(lambda : defaultdict(bool))
    answer = []
    count = 0

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def dfs(y, x):
        nonlocal memo, N, H, count, direction
        for d in direction:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < N and 0 <= nx < N:
                if H[ny][nx] == '1' and memo[ny][nx] == False:
                    count += 1
                    memo[ny][nx] = True
                    dfs(ny, nx)


    for y in range(N):
        for x in range(N):
            count = 0
            if memo[y][x] == False and H[y][x] == '1':
                memo[y][x] = True
                count += 1
                dfs(y, x)
            if count != 0: answer.append(count)

    print(len(answer))
    for a in answer:
        print(a)


solution()

