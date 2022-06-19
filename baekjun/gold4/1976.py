import sys 
input = sys.stdin.readline

from collections import defaultdict

def solution():
    N = int(input())
    M = int(input())
    D = defaultdict(lambda : defaultdict(lambda : float('INF'))) #distance

    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j] == 1:
                D[i + 1][j + 1] = 1
                D[j + 1][i + 1] = 1

    P = list(map(int, input().split())) 

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i + 1][j + 1] = min(D[i + 1][j + 1], D[i + 1][k + 1] + D[k + 1][j + 1])
    
    for i in range(M - 1):
        start, end = P[i], P[i + 1]
        if D[start][end] == float('INF') and start != end:
            return "NO"

    return "YES"

print(solution())


# import sys 
# input = sys.stdin.readline

# from collections import defaultdict

# def solution():
#     N = int(input())
#     M = int(input())
#     C = defaultdict(set)

#     for i in range(N):
#         temp = list(map(int, input().split()))
#         for j in range(N):
#             if temp[j] == 1:
#                 C[i + 1].add(j + 1)
#                 C[j + 1].add(i + 1)

#     P = list(map(int, input().split()))

#     vi_n = defaultdict(bool) #node 방문 여부 
#     vi_e = defaultdict(lambda:defaultdict(bool)) #edge 방문 여부 
#     link = False

#     def dfs(now, end):
#         nonlocal vi_n, vi_e, C, link

#         for next in C[now]:
#             if not vi_e[now][next]: #해당 엣지에 방문해본 경험이 없음
#                 vi_n[next] = True #다음 노드 True
#                 vi_e[now][next] = True

#                 if vi_n[end]:
#                     link = True
#                 else:
#                     dfs(next, end)
#             else:
#                 if vi_n[end]:
#                     link = True


#     for st_idx in range(M - 1):
#         link = False
#         start, end = P[st_idx], P[st_idx + 1]
#         dfs(start, end)

#         if not link and start != end:
#             print("NO")
#             return 

#     print("YES")
    

# solution()


