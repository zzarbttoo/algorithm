from collections import defaultdict
import heapq

def solution():

    N = int(input())
    S = []
    C = defaultdict(list)
    answer = 0

    for _ in range(N):
        S.append(list(map(float, input().split())))
    
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = ((S[i][0] - S[j][0]) ** 2 + (S[i][1] - S[j][1]) ** 2) ** 0.5
                C[i].append([dist, j])
                C[j].append([dist, i])
    
    heap = []
    visited = defaultdict(bool)

    heapq.heappush(heap, [0, 0])

    while heap:
        dist, node = heapq.heappop(heap)

        if not visited[node]:
            answer += dist
            visited[node] = True
        else:
            continue

        for next in C[node]:
            if not visited[next[1]]:
                heapq.heappush(heap, next)





    print(answer)



        



solution()