
# 함수를 만들어서 진행할 경우 시간 초과(global, nonlocal의 차이)
# direction의 방향이 좌/우 부터 시작하지 않을 경우 시간 초과 
# https://www.acmicpc.net/board/view/85390
# set 대신 defaultdict를 사용할 경우 시간 초과
# set에서 not ~~ in ~~ 가 아니라 ~~~ not in ~~~ 로 진행할 경우 시간초과 
# recursion에 대한 제안을 둘 경우 시간 초과 


from sys import stdin

R, C = map(int, stdin.readline().split())
A = []
for _ in range(R):
    A.append(list(stdin.readline()))

#di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#di = [[0, 1], [0, -1], [-1, 0], [1, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

vi = set()

answer = 0

def dfs(y, x, cnt):
    global answer 
    answer = max(answer, cnt)
    
    for i in range(4):
        ny, nx = y + dy[i] , x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and not A[ny][nx] in vi:
            vi.add(A[ny][nx])
            #vi[A[ny][nx]] = True
            dfs(ny, nx, cnt + 1)
            #vi[A[ny][nx]] = False
            vi.remove(A[ny][nx])

vi.add(A[0][0])
dfs(0, 0, 1)

print(answer)



# from sys import stdin
# from collections import defaultdict

# R, C = map(int, stdin.readline().split())
# A = []
# for _ in range(R):
#     A.append(list(stdin.readline()))

# #di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# #di = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# vi = defaultdict(bool)

# answer = 0

# def dfs(y, x, cnt):
#     global answer 
#     answer = max(answer, cnt)
    
#     for i in range(4):
#         ny, nx = y + dy[i] , x + dx[i]
#         if 0 <= ny < R and 0 <= nx < C and vi[A[ny][nx]] == False:
#             #vi.add(A[ny][nx])
#             vi[A[ny][nx]] = True
#             dfs(ny, nx, cnt + 1)
#             vi[A[ny][nx]] = False
#             #vi.remove(A[ny][nx])

# vi[A[0][0]] = True
# dfs(0, 0, 1)

# print(answer)




# from sys import stdin
# from collections import defaultdict

# def solution():
#     R, C = map(int, stdin.readline().split())
#     A = []
#     for _ in range(R):
#         A.append(list(stdin.readline()))
    
#     #di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     #di = [[0, 1], [0, -1], [-1, 0], [1, 0]]

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     vi = defaultdict(bool)

#     answer = 0

#     def dfs(y, x, cnt):
#         nonlocal answer, R, C, A, vi
#         answer = max(answer, cnt)
        
#         for i in range(4):
#             ny, nx = y + dy[i] , x + dx[i]
#             if 0 <= ny < R and 0 <= nx < C and vi[A[ny][nx]] == False:
#                 #vi.add(A[ny][nx])
#                 vi[A[ny][nx]] = True
#                 dfs(ny, nx, cnt + 1)
#                 vi[A[ny][nx]] = False
#                 #vi.remove(A[ny][nx])

#     vi[A[0][0]] = True
#     dfs(0, 0, 1)

#     print(answer)

# solution()

