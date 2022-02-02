# from sys import stdin
# from collections import defaultdict
# from collections import deque 

# def input_nums():

#     N, M = map(int, stdin.readline().split())
#     room = []

#     for _ in range(N):
#         room.append(stdin.readline())
#     return N, M, room 

# def solution():
#     N, M, room = input_nums()
#     visited =  defaultdict(lambda : defaultdict(lambda : defaultdict(int)))  #0으로 초기화 
#     q = deque([])
#     direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#     visited[0][0][1] = 1 
#     visited[0][0][0] = 1 
#     q.append([0, 0, 0])

#     while q:
#         temp = q.popleft()
#         x, y, w = temp[0], temp[1], temp[2]
#         if x == N - 1 and y == M - 1:
#             print(visited[x][y][w] + 1)
#             return

#         for direct in direction:
#             nx, ny = x + direct[0], y + direct[1]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if room[nx][ny] == '1' and w == 0:
#                     visited[nx][ny][1] = visited[nx][ny][0] + 1
#                     q.append([nx, ny, 1])
#                 elif room[nx][ny] == '0' and visited[nx][ny][w] == 0:
#                     visited[nx][ny][w] = visited[x][y][w] + 1
#                     q.append([nx, ny, w])

#     print(-1)

# solution()

# from collections import deque 
# from sys import stdin

# def input_nums():

#     N, M = map(int, stdin.readline().split())
#     room = []

#     for _ in range(N):
#         room.append(stdin.readline())
#     return N, M, room 


# from collections import defaultdict

# def solution():
#     #N, M, room = input_nums()

#     N, M = 8, 8
#     room = ["01000100", "01010100" , "01010100", "01010100", "01010100", "01010100", "01010100", "00010100"]

#     answer = 0
#     queue = deque([])
#     dist = [[[float('INF')] * 2 for _ in range(M)] for __ in range(N)]

#     visited = defaultdict(lambda : defaultdict(bool))

#     direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

#     queue.append([(0, 0), False, 0]) #now, break(bool), length
#     dist[0][0][0] = 0
#     visited[0][0] = True

#     #0, 0 -> N-1, N-1
#     while queue:
#         now = queue.popleft()
#         print("now ::: " + str(now))
#         loc, is_break, length = now[0], now[1], now[2]
#         print("dist ::: " + str(length))

#         if loc[0] == N-1 and loc[1] == M-1:
#             answer = dist[loc[0]][loc[1]][is_break] + 1 #정답 출력
#             break
            
#         for direct in direction:
#             next = (loc[0] + direct[0], loc[1] + direct[1])
#             if 0 <= next[0] < N and 0 <= next[1] < M and visited[next[0]][next[1]] == False:
#                 if room[next[0]][next[1]] == '0' and dist[next[0]][next[1]][is_break] == float('INF'):
#                     dist[next[0]][next[1]][is_break] = length + 1
#                     visited[next[0]][next[1]] = True
#                     queue.append([next, is_break , length + 1])
#                 elif is_break == False and room[next[0]][next[1]] == '1' and dist[next[0]][next[1]][True] == float('INF'):
#                     dist[next[0]][next[1]][True] = length + 1
#                     visited[next[0]][next[1]] = True
#                     queue.append([next, True , length + 1])

#     if answer == 0:
#         print(-1)
#     else:
#         print(answer)

# solution()