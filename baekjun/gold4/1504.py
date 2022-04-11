
from collections import defaultdict
import heapq

def solution():

    N, E = map(int, input().split())
    G = defaultdict(list)

    for _ in range(E):
        a, b, c = map(int, input().split())
        G[a].append([c, b])
        G[b].append([c, a])
    
    V1, V2 = map(int, input().split())

    def dijk(start, end):

        nonlocal G, N
        D = defaultdict(lambda : float('INF'))
        visited = defaultdict(bool)
        heap = [[0, start]] #처음 

        while heap:

            now = heapq.heappop(heap)

            if not visited[now[1]]:
                visited[now[1]] = True
                if D[now[1]] > now[0]:
                    D[now[1]] = now[0]

                for next in G[now[1]]:
                    n_c = next[0] + D[now[1]]
                    if D[next[1]] > n_c:
                        D[next[1]] = n_c
                        heapq.heappush(heap, [n_c, next[1]])
        
        return D[end]


    answer = min(dijk(1, V1) + dijk(V1, V2) + dijk(V2, N), dijk(1, V2) + dijk(V2, V1) + dijk(V1, N))

    if answer == float('INF'): print(-1)
    else: print(answer)

solution()


# def solution():
#     N, E = map(int, input().split())

#     G = defaultdict(list)

#     for _ in range(E):
#         a, b, c = map(int, input().split())
#         G[a].append([c, b])
#         G[b].append([c, a])
    
#     V1, V2 = map(int, input().split())

#     vi = defaultdict(bool)  

#     heap = [[0, 1]]
#     answer = 0

#     while heap:

#         if vi[V1] and vi[V2] and vi[N]:
#             return answer 

#         now = heapq.heappop(heap)

#         if not vi[now[1]]:
#             vi[now[1]] = True
#             answer += now[0]

#             for next in G[now[1]]:
#                 heapq.heappush(heap, next)
    
#     return -1 
            
# print(solution())