
from collections import defaultdict

def solution():

    N, D = map(int, input().split())

    dist = defaultdict(int)
    cut = defaultdict(list)

    for _ in range(N):
        start, end, d = map(int, input().split())
        cut[end].append([start, d]) #start, dist

    for i in range(1, D + 1):
        dist[i] = dist[i - 1] + 1
        for c in cut[i]:
            if dist[c[0]] + c[1] < dist[i]:
                dist[i] = dist[c[0]] + c[1]
    
    print(dist[D])

solution()
