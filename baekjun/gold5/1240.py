# from collections import defaultdict

# def solution():
#     answer = 0
#     N, M = map(int, input().split())
#     n_list, m_list = [], []

#     for _ in range(N - 1):
#         n_list.append(list(map(int, input().split())))

#     for _ in range(M):
#         m_list.append(list(map(int, input().split())))


#     def get_distance(N, n_list):
#         distance = defaultdict(lambda: defaultdict(lambda : float("INF")))

#         for n in n_list:
#             if n[2] < distance[n[0]][n[1]]:
#                 distance[n[0]][n[1]] = n[2]
#             if n[2] < distance[n[1]][n[0]]:
#                 distance[n[1]][n[0]] = n[2]


#         for k in range(1, N + 1):
#             for i in range(1, N + 1):
#                 for j in range(1, N + 1):
#                     distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

#         return distance



#     def calculate_distance(m_list, distance):
#         for m in m_list:
#             print(distance[m[0]][m[1]])

#     distance = get_distance(N, n_list) 
#     calculate_distance(m_list, distance)
    


# solution()
#print(solution())

from collections import defaultdict
from queue import Queue

def solution():
    N, M = map(int, input().split())
    link_hash = defaultdict(list)

    for _ in range(N - 1):
        start, end, weight = map(int, input().split())
        link_hash[start].append([end, weight])
        link_hash[end].append([start, weight])

    def search(start, end):

        nonlocal link_hash

        queue = Queue()
        visited = defaultdict(int)

        queue.put([start, 0])
        visited[start] = 1

        while queue:
            now, distance = queue.get()

            if now == end:
                return distance

            for next, weight in link_hash[now]:
                if visited[next] == 0:
                    visited[next] = 1
                    queue.put([next, weight + distance])

    for _ in range(M):
        start, end = map(int, input().split())
        print(search(start, end))


solution()