from sys import stdin

def input_nums():

    N, M = map(int, stdin.readline().split())
    room = []

    for _ in range(N):
        room.append(input())
    return N, M, room 


from queue import Queue
from collections import defaultdict

def solution():
    N, M, room = input_nums()

    queue = Queue()
    dist = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : float('INF'))))
    visited = defaultdict(lambda : defaultdict(bool))

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

    queue.put([(0, 0), False, 0]) #now, break(bool), length
    dist[0][0][0] = 0
    visited[0][0] = True

    count = 0
    #0, 0 -> N-1, N-1
    while queue.qsize():
        now = queue.get()
        loc, is_break, length = now[0], now[1], now[2]

        if loc[0] == N-1 and loc[1] == M-1:
            print(dist[loc[0]][loc[1]][is_break] + 1) #정답 출력
            return 
            
        for direct in direction:
            next = (loc[0] + direct[0], loc[1] + direct[1])
            if 0 <= next[0] < N and 0 <= next[1] < M and visited[next[0]][next[1]] == False:
                if room[next[0]][next[1]] == '0' and dist[next[0]][next[1]][is_break] == float('INF'):
                    dist[next[0]][next[1]][is_break] = length + 1
                    visited[next[0]][next[1]] = True
                    queue.put([next, is_break , length + 1])
                if is_break == False and room[next[0]][next[1]] == '1' and dist[next[0]][next[1]][True] == float('INF'):
                    dist[next[0]][next[1]][True] = length + 1
                    visited[next[0]][next[1]] = True
                    queue.put([next, True , length + 1])

    print(-1)

solution()