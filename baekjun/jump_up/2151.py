from sys import stdin

def input_():
    N = int(stdin.readline())
    M = []

    for _ in range(N):
        M.append(stdin.readline().strip())

    return N, M

from collections import deque
from collections import defaultdict

def solution():
    N, M = input_()
    #N, M = 5, ["***#*", "*.!.*", "*!.!*", "*.!.*", "*#***"]

    count = 0
    start, end = [], []
    for x in range(N):
        for y in range(N):
            if count == 0 and M[x][y] == '#':
                start = [x, y]
                count += 1
            elif count == 1 and M[x][y] == "#":
                end = [x, y]

    que = deque([])

    direction = [[-1, 0], [0, -1], [0, 1], [1, 0]] 
    op = {0 : [1, 2], 1 : [0, 3], 2 : [0, 3], 3 : [1, 2]}

    for idx, d in enumerate(direction):
        next = [d[0] + start[0], d[1] + start[1]]
        if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
            if M[next[0]][next[1]] == "." or M[next[0]][next[1]] == "!":
                que.append([next, 0, idx])
            if M[next[0]][next[1]] == "!":
                que.append([next, 1, idx])
    

    while que:
        temp = que.popleft()
        now, count, before = temp[0], temp[1], temp[2]

        if now == end:
            print(count)

        #안 할 경우
        if M[now[0]][now[1]] == "." or M[now[0]][now[1]] == "!":
            b_d = direction[before]
            next = [now[0] + b_d[0], now[1] + b_d[1]]
            if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
                que.append([next, count, before])

        #거울을 설치 할 경우
        if M[now[0]][now[1]] == "!":
            for idx in op[before]:
                nd = direction[idx]
                next = [now[0] + nd[0], now[1] + nd[1]]
                if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
                    que.append([next, count + 1, idx])



solution()


# 문제 잘 못 이해함 ^^^ㅜㅜ
# from collections import deque
# from collections import defaultdict

# def solution():
#     N, M = input_()
#     #N, M = 5, ["***#*", "*.!.*", "*!.!*", "*.!.*", "*#***"]

#     count = 0
#     start, end = [], []
#     for x in range(N):
#         for y in range(N):
#             if count == 0 and M[x][y] == '#':
#                 start = [x, y]
#                 count += 1
#             elif count == 1 and M[x][y] == "#":
#                 end = [x, y]

#     direction = [[-1, -1], [1, -1], [-1, 1], [1, 1]]
#     op = {0 : [1, 2], 1 : [0, 3], 2 : [1, 3], 3 : [1, 2]}

#     que = deque([])

#     for idx, d in enumerate(direction):
#         next = [d[0] + start[0], d[1] + start[1]]
#         if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
#             if M[next[0]][next[1]] == "." or M[next[0]][next[1]] == "!":
#                 que.append([next, 0, idx])
#             if M[next[0]][next[1]] == "!":
#                 que.append([next, 1, idx])

#     while que:
#         temp = que.popleft()
#         now , count, before = temp[0], temp[1], temp[2]

#         if [now[0], now[1]] == end:
#             return count

#         #안 할 경우
#         if M[now[0]][now[1]] == "." or M[now[0]][now[1]] == "!":
#             b_d = direction[before]
#             next = [now[0] + b_d[0], now[1] + b_d[1]]
#             if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
#                 que.append([next, count, before])

#         #거울을 설치 할 경우
#         if M[now[0]][now[1]] == "!":
#             for idx in op[before]:
#                 nd = direction[idx]
#                 next = [now[0] + nd[0], now[1] + nd[1]]
#                 if 0 <= next[0] < N and 0 <= next[1] < N and M[next[0]][next[1]] != "*":
#                     que.append([next, count + 1, idx])

# print(solution())
