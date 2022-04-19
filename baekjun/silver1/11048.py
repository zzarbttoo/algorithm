from collections import defaultdict


def solution():
    N, M = map(int, input().split())
    P = []

    for _ in range(N):
        P.append(list(map(int, input().split())))
    
    count = defaultdict(lambda : defaultdict(int))
    direction = [[0, -1], [-1, 0], [-1, -1]]

    for y in range(N):
        for x in range(M):
            for d in direction:
                by, bx = d[0] + y, d[1] + x
                if count[y][x] < count[by][bx] + P[y][x]:
                    count[y][x] = count[by][bx] + P[y][x]

    print(count[N-1][M-1])

solution()






# from collections import defaultdict

# def solution():
#     N, M = map(int, input().split())
#     P = []

#     for _ in range(N):
#         P.append(list(map(int, input().split())))
    
#     visited = defaultdict(lambda : defaultdict(bool))
#     answer = -1
#     direction = [[1, 0], [0, 1],[0, -1]]

#     def dfs(y, x, count):

#         nonlocal visited, answer, direction, P

#         for d in direction:
#             ny, nx = y + d[0], x + d[1]
#             if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
#                 print(ny, nx, count + P[ny][nx])
#                 visited[ny][nx] = True
#                 if ny == N - 1 and nx == M - 1:
#                     answer = max(answer, count + P[ny][nx])
#                 else:
#                     dfs(ny, nx, count + P[ny][nx])
#                 visited[ny][nx] = True
#     visited[0][0] = True

#     dfs(0, 0, P[0][0])
#     print(answer)


# solution()