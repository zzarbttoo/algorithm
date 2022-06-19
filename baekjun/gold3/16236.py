# from re import A
# from sys import stdin
# input = stdin.readline

# from collections import deque
# from collections import defaultdict

# def solution():

#     answer = 0
#     N:int = int(input())
#     A:list = []
#     for _ in range(N):
#         A.append(list(map(int, input().split())))

#     queue = deque([])
#     sh:int = 2
#     direct:list = [[0, 1], [1, 0], [-1, 0], [0, -1]] 
#     cnt:int = 0

#     for y in range(N):
#         for x in range(N):
#             if A[y][x] == 9: break

#     queue.append([sh, cnt, [y, x], A]) #현재 크기, 이동횟수, 현재 위치(y, x)
#     A[y][x] = 0
#     print("A :::" + str(A))
#     print("y, x" + str(y) + ":" + str(x))

#     while queue:
#         sh, cnt, [y, x], now_A = queue.popleft()
#         print(sh, cnt, y, x, now_A)

#         for di in direct:
#             ny, nx = y + di[0], x + di[1]
#             if 0 <= ny < N and 0 <= nx < N:
#                 if now_A[ny][nx] != 0:
#                     if now_A[ny][nx] < sh:
#                         n_fish_size = now_A[ny][nx]
#                         now_A[ny][nx] = 0
#                         queue.append([sh + 1, cnt + 1, [ny, nx], now_A])
#                         print("1")
#                         now_A[ny][nx] = n_fish_size
#                     elif now_A[ny][nx] == sh and now_A[ny][nx] != 0:
#                         print("2")
#                         queue.append([sh, cnt + 1, [ny, nx], now_A])
#                 else:
#                     if answer < cnt:
#                         print("3")
#                         answer = cnt

#     print(answer)

# solution()


#문제 잘못 이해함 

