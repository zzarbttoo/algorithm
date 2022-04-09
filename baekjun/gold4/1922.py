import heapq
from collections import defaultdict

def solution():
    N = int(input())
    M = int(input())

    C = defaultdict(list)
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        C[a].append([c, b])
        C[b].append([c, a])

    heap = [[0, 1]]   
    visited = defaultdict(bool)
    answer, cnt = 0, 0

    while heap:
        now = heapq.heappop(heap)
        weight, node = now[0], now[1]

        if cnt == N:
            break
        
        if not visited[node] :

            visited[node] = True
            cnt += 1
            answer += weight

            for next in C[node]:
                heapq.heappush(heap, next)
    
    print(answer)

solution()