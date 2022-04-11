from collections import defaultdict
import heapq

def solution():
    V, E = map(int, input().split())
    L = defaultdict(list)

    for _ in range(E):
        A, B, C = map(int, input().split())
        L[A].append([C, B])
        L[B].append([C, A])

    cnt, answer = 0, 0
    heap = [[0, 1]]

    visited = defaultdict(bool)

    while heap:
        now = heapq.heappop(heap)
        weight, node = now[0], now[1]

        if cnt == V:
            break

        if visited[node] == False:
            visited[node] = True
            cnt += 1
            answer += weight

            for next in L[node]:
                heapq.heappush(heap, next)

    print(answer)

solution()




