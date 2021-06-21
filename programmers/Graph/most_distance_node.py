import collections
import heapq
def solution(n, edge):

    dist = collections.defaultdict(int)
    graph = collections.defaultdict(list)

    Q = [1] #거리는 0, 노드는 1 부터 시작
    dist[1] = 0
    for node in edge:
        graph[min(node)].append(max(node))
    

    while Q:
        now_node = heapq.heappop(Q) #최소 값 출력
        for node in graph[now_node]:
            if dist[node] == 0:
                next_distance = dist[now_node] + 1
                dist[node] = next_distance
                heapq.heappush(Q, node)

    
    num = collections.defaultdict(int)

    for i in dist:
        num[dist[i]] +=1
    
    return num[max(num)]
    


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))