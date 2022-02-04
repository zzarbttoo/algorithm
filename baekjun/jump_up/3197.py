from sys import stdin
def input_nums():
    R, C = map(int, stdin.readline().split())
    W = []
    for _ in range(R):
        W.append(list(stdin.readline().strip()))

    return R, C, W

import copy
from collections import deque
from collections import defaultdict

def solution():

    R, C, W = input_nums()
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def start_end():

        nonlocal W
        count = 0

        start, end = [], []

        for r in range(R):
            for c in range(C):
                if W[r][c] == 'L':
                    if count == 0:
                        start = [r, c]
                    else:
                        end = [r, c]
                        return start, end
                    count += 1
        
    start, end = start_end()

    def new_ice(W):

        nonlocal R, C, direction

        nextW = copy.deepcopy(W)

        for r in range(R):
            for c in range(C):
                if W[r][c] == '.':
                    for direct in direction:
                        nextX, nextY = direct[0] + r, direct[1] + c
                        if 0 <= nextX < R and 0 <= nextY < C:
                            if W[nextX][nextY] == 'X':
                                nextW[nextX][nextY] = '.'
        return nextW


    answer = -1

    count = 0


    while answer == -1:

        queue = deque([start])
        visited = defaultdict(lambda : defaultdict(bool))
        visited[start[0]][start[1]] = True

        while queue and answer == -1:

            now = queue.popleft()

            for direct in direction:
                    nextX, nextY = direct[0] + now[0], direct[1] + now[1]
                    if 0 <= nextX < R and 0 <= nextY < C and W[nextX][nextY] != 'X':
                        if end[0] == nextX and end[1] == nextY:
                            answer = 1
                            break
                        else:
                            if visited[nextX][nextY] == False:
                                queue.append([nextX, nextY])
                                visited[nextX][nextY] = True

        if answer != -1:
            break

        W = new_ice(W)
        count += 1

    print(count)   


solution()
