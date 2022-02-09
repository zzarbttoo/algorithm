from sys import stdin
def input_():
    M, N, H = map(int, stdin.readline().split())

    B = []

    for _ in range(H):
        R = []
        for _ in range(N):
            R.append(list(map(int, stdin.readline().split())))
        B.append(R)
    return M, N, H, B

from copy import deepcopy
from collections import deque

def solution():
    M, N, H, B = input_()

    que = deque([])
    direction = [
        [-1, 0, 0], [1, 0, 0], 
        [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]
    ]

    cnt = 0
    time = 0
    l_cnt = 0

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if B[h][n][m] == 1:
                    que.append([h, n, m])
                if B[h][n][m] == 0:
                    cnt += 1
                if B[h][n][m] == 0 or B[h][n][m] == -1:
                    l_cnt += 1

    if cnt == 0: return time
    if l_cnt == (H * N * M): return -1

    while que:
        time += 1
        b_c = cnt
        temp = len(que)
        for _ in range(temp):
            now = que.popleft()
            h, n, m = now[0], now[1], now[2]
            for d in direction:
                n_h, n_n, n_m = h + d[0], n + d[1], m + d[2]
                if 0 <= n_h < H and 0 <= n_n < N and 0 <= n_m < M:
                    if B[n_h][n_n][n_m] == 0: 
                        cnt -= 1
                        B[n_h][n_n][n_m] = 1
                        que.append([n_h, n_n, n_m])

        if cnt == 0: return time
        if b_c == cnt: return -1

print(solution())

#시간 초과
# def solution():
#     M, N, H, B = input_()

#     # M, N, H, B = 5, 3, 2, [
#     #     [
#     #         [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
#     #     ], 
#     #     [
#     #         [0, 0, 0, 0, 0, 0], [0, 0, 1, 0 ,0], [0, 0, 0, 0, 0]
#     #     ]
#     # ]
    

#     direction = [
#         [-1, 0, 0], [1, 0, 0], 
#         [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]
#     ]
#     def ripe(B):
#         nonlocal M, N, H
#         n_b = deepcopy(B)
#         cnt = 0

#         for h in range(H):
#             for n in range(N):
#                 for m in range(M):
#                     if B[h][n][m] == 0:
#                         for d in direction:
#                             n_h, n_n, n_m = h + d[0], n + d[1], m + d[2]
#                             if 0 <= n_h < H and 0 <= n_n < N and 0 <= n_m < M:
#                                 if B[n_h][n_n][n_m] == 1: 
#                                     n_b[h][n][m] = 1
#                                     break
#                     if n_b[h][n][m] == 0: cnt += 1

#         return n_b, cnt 

#     cnt = 0
#     time = 0

#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if B[h][n][m] == 0:
#                     cnt += 1
    
#     if cnt == 0: return time

#     while True:
#         time += 1
#         n_B, cnt = ripe(B)

#         if cnt == 0: return time
#         if B == n_B: 
#             return -1
#         B = n_B



# print(solution())

