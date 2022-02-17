from sys import stdin
from collections import defaultdict

def input_():
    V, E = map(int, stdin.readline().split())
    S = int(stdin.readline())
    L = defaultdict(lambda : defaultdict(int))

    for _ in range(E):
        t1, t2, t3 = map(int, stdin.readline().split())
        L[t1][t2] = t3 #u -> v
   
    return V, E, S, L

from queue import PriorityQueue

def solution():
    V, E, S, L = input_()
    
    A = defaultdict(lambda : float('INF'))
    visited = defaultdict(bool)
    que = PriorityQueue()

    A[S] = 0

    que.put([0, S])

    while que.qsize() != 0:
        now = que.get()[1]

        visited[now] = True
        for next in L[now].keys():
            if A[next] > A[now] + L[now][next]:
                A[next] = A[now] + L[now][next]
                if visited[next] == False: 
                    que.put([A[next], next])

    for i in range(1, V + 1):
        if A[i] == float('INF'): print("INF")
        else: print(A[i])

solution()

