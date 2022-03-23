#치킨 먹고 싶다 

import itertools 

def solution():
    N, M = map(int, input().split())
    T = []

    for _ in range(N):
        T.append(list(map(int, input().split())))
    
    C = []
    H = []

    for y in range(N):
        for x in range(N):
            if T[y][x] == 1:
                H.append([y, x])
            if T[y][x] == 2:
                C.append([y, x])
    
    m_l = list(itertools.combinations(C, M))

    answer = float('INF')

    for m in m_l:
        t = sum([min([abs(h[0]- c[0]) + abs(h[1] - c[1]) for c in m]) for h in H])
        if answer > t: answer = t
    print(answer)

    if answer == float('INF'): print(-1)


    
solution()





