
from collections import defaultdict
from queue import Queue

input = __import__('sys').stdin.readline

def solution():

    link = defaultdict(lambda : defaultdict(int))
    dist = defaultdict(lambda : defaultdict(lambda : float('INF')))

    N, M, K = map(int, input().split())

    for _ in range(M):
        n1, n2, length = map(int, input().split())
        link[n1][n2], link[n2][n1] = length, length

    #1부터 시작
    queue = Queue()

    #now, k_cnt, weight = 1, 0, 0
    dist[1][0] = 0

    queue.put([1, 0, 0])

    while queue.qsize() > 0:
        before = queue.get()
        now, k_cnt, weight = before[0], before[1], before[2]

        if dist[now][k_cnt] < weight:
            continue
        dist[now][k_cnt] = weight

        if now >= N or k_cnt >= K: continue

        for next in link[now].keys():
            if link[now][next] != 0: 
                if dist[next][k_cnt] > weight + link[now][next]:
                    dist[next][k_cnt] = weight + link[now][next]
                    queue.put([next, k_cnt, weight + link[now][next]])
                if k_cnt < K and dist[next][k_cnt + 1] > weight:
                    dist[next][k_cnt + 1] = weight
                    queue.put([next, k_cnt + 1, weight])

    print(min(dist[N].values()))    
        
solution()







# from collections import defaultdict
# from queue import Queue

# def solution():
#     link = defaultdict(lambda : defaultdict(lambda : -1))
#     dist = defaultdict(lambda : defaultdict(lambda : float('INF')))

#     N, M, K = map(int, input().split())

#     queue = Queue()

#     for _ in range(M):
#         c1, c2, di = map(int, input().split())
#         link[c1][c2], link[c2][c1] = di, di

#     wei, now, cnt = 0, 1, 0
#     dist[now][cnt] = wei
#     queue.put([wei, now, cnt]) #weight, nownum, k_count

#     while queue.qsize() > 0:
#         before = queue.get()
#         wei, now, cnt = before[0], before[1], before[2]

#         if dist[now][cnt] < wei:
#             continue

#         dist[now][cnt] = wei

#         for next in link[now].keys():
#             if link[now][next] != -1:
#                 next_wei = wei + link[now][next]
#                 if dist[next][cnt] > next_wei:
#                     dist[next][cnt] = next_wei
#                     queue.put([next_wei, next, cnt])

#                 if cnt < K and dist[next][cnt] > wei:
#                     dist[next][cnt + 1] = wei #다음으로 가는 가중치 제거
#                     queue.put([wei, next, cnt + 1])

#     print(dist)

# solution()


# from collections import defaultdict
# from queue import Queue

# def solution():

#     link = defaultdict(lambda : defaultdict(lambda : -1))
#     N, M, K = map(int, input().split())
#     candidate = []
#     queue = Queue()

#     for _ in range(M):
#         c1, c2, dist = map(int, input().split())
#         link[c1][c2], link[c2][c1] = dist, dist
    
#     visited = [0 for _ in range(N + 1)] #init 0 visited = -1
#     dist = []

#     now = 1
#     visited[1] = -1

#     queue.put([visited, now, dist])

#     while queue.qsize() > 0:
#         before = queue.get()
#         v, n, d = before[0], before[1], before[2]

#         if n == N:
#             candidate.append(d)
#             continue

#         for key in link[n].keys():
#             n_v = v[:]
#             if link[n][key] != -1 and n_v[key] == 0:
#                 n_v[key] = -1 
#                 n_d = d[:]
#                 n_d.append(link[n][key])
#                 queue.put([n_v, key, n_d])
    
#     answer = float('INF')

    # for can in candidate:
    #     can.sort(reverse = True)
    #     for i in range(K):
    #         if can[i]: can[i] = 0
    #     sum_c = sum(can)
    #     if answer > sum_c: answer = sum_c
    
    # print(answer)

#solution()


# from collections import defaultdict

# import sys
# sys.setrecursionlimit(10 ** 5)

# def solution():

#     link = defaultdict(lambda : defaultdict(lambda : -1))
#     N, M, K = map(int, input().split())
#     candidate = []

#     for _ in range(M):
#         c1, c2, dist = map(int, input().split())
#         link[c1][c2], link[c2][c1] = dist, dist
    
#     visited = [0 for _ in range(N + 1)] #init 0 visited = -1
#     dist = []
#     now = 1

#     def dfs(now, visited, dist):
#         nonlocal link, candidate

#         if now == N: 
#             candidate.append(dist)
#             return 

#         for key in link[now].keys():
#             n_v = visited[:]
#             if link[now][key] != -1 and n_v[key] == 0:
#                 n_v[key] = -1 
#                 n_d = dist[:]
#                 n_d.append(link[now][key])
#                 dfs(key, n_v, n_d)


#     visited[now] = -1
#     dfs(now ,visited, dist)

#     answer = float('INF')

#     for can in candidate:
#         can.sort(reverse = True)
#         for i in range(K):
#             if can[i]: can[i] = 0
#         sum_c = sum(can)
#         if answer > sum_c: answer = sum_c
    
#     print(answer)

# solution()
