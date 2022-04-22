
from collections import defaultdict
import heapq

def solution(n, start, end, roads, traps):
    
    traps = set(traps)
    l = defaultdict(list)
    
    for road in roads:
        l[road[0]].append([road[2], road[1], 0])
        l[road[1]].append([road[2], road[0], 1])
    
    v = defaultdict(lambda : defaultdict(lambda : float('INF')))
    heap = []
    
    heapq.heappush(heap, [0, start, 0]) #가중치, 노드, 스위치
    
    while heap:
        wei, now, sw = heapq.heappop(heap)
        if now == end:
            return wei
        
        if now in traps: #toggle
            sw ^= (1 << now)
        
        if v[now][sw] > wei: 
            v[now][sw] = wei
        else: 
            continue
        
        for next in l[now]:
            next_wei = wei + next[0]
            #둘다 켜져있거나/꺼져 있거나 
            if ((sw & (1 << now)) == 0 and (sw & (1 << next[1])) == 0) or ((sw & (1 << now)) != 0 and (sw & (1 << next[1])) != 0): #둘다 꺼짐: #둘다 꺼짐
                if next[2] == 0:
                    heapq.heappush(heap, [next_wei, next[1] ,sw])
            else: #하나만 켜져있음
                if next[2] == 1:
                    heapq.heappush(heap, [next_wei, next[1] ,sw])

# from collections import defaultdict
# import copy

# def solution(n, start, end, roads, traps):
    
#     is_trap = defaultdict(int)
#     travel = defaultdict(lambda : defaultdict(list))
    
#     for trap in traps:
#         is_trap[trap] = 1
        
#     for road in roads:
#         travel[road[0]][road[1]] = [road[2], 1]
#         travel[road[1]][road[0]] = [road[2], -1]
        
    
#     min_time = 3000001
    
    
#     def search(now_node, now_travel , now_time):
        
#         nonlocal min_time
        
#         #함정일 경우 뒤집기 처리
#         if is_trap[now_node] == 1:
#             for key, value in now_travel[now_node].items():
#                 now_travel[now_node][key][1] *= -1
#                 now_travel[key][now_node][1] *= -1
        
#         if now_node == end:
#             min_time = min(min_time, now_time)
        
#         for key, value in now_travel[now_node].items():
#             if value[1] == 1:
#                 next_travel = copy.deepcopy(now_travel)
#                 next_time = now_time + value[0]
#                 next_travel[now_node][key][1] = 0
                
#                 search(key, next_travel, next_time)
            
        
#     for key, value in travel[start].items():
#         time = value[0]
#         temp_travel = copy.deepcopy(travel)
#         temp_travel[start][key][1] = 0
#         search(key , temp_travel, time)
        
#     return min_time

# from collections import defaultdict
# import heapq

# INF = 999999999

# def solution(n, start, end, roads, traps):
    
    
#     graph = [[INF for _ in range(n + 1)] for _ in range(n+1)]
#     is_trap = defaultdict(int)

#     # 1은 trap 발동, -1은 trap 안발동, 0은 trap이 아님
#     for trap in traps:
#         is_trap[trap] = -1

#     first_state = "-1" * len(traps)

#     for i in range(1, n + 1):
#         graph[i][i] = 0

#     for road in roads:
#         now_node = road[0]
#         next_node = road[1]
#         node_weight = road[2]

#         if node_weight <= graph[now_node][next_node]:
#             graph[now_node][next_node] = node_weight

#     def dijkstra():

#         priority = []
#         visited = defaultdict(lambda : defaultdict(int))
        
#         #cost(priority), node, state(trap)
#         priority.append((-1 , 0, start, first_state))

#         while priority:
            
#             current =  heapq.heappop(priority)
#             before_node, weight, now_node, state = current[0], current[1], current[2], current[3]

#             print("before_node ::: "  + str(before_node) + "now_node ::: " + str(now_node))
#             print("is_trap ::: " + str(is_trap))

#             if now_node == end:
#                 return weight

#             #방문한 적이 있다면 넘어간다 
#             # if visited[now_node][state] == 1:
#             #     print("hello again")
#             #     continue
                
#             visited[now_node][state] = 1


#             # trap을 켜면 1로 바꿔준다 
#             if is_trap[now_node] != 0:
#                 is_trap[now_node] *= -1
#                 state = ""
#                 for key, value in is_trap.items():
#                     if value != 0:
#                         state += str(is_trap[key])

#             print(visited)
#             # if visited[now_node][state] == 1:
#             #     print("helloworld 2")
#             #     continue

#             visited[now_node][state] = 1
#             for next_node in range(1, n + 1):

#                 if now_node == next_node:
#                     continue
                
#                 #둘중 하나만 함정이 작동
#                 if (is_trap[now_node] == 1 and is_trap[next_node] != 1) or (is_trap[now_node] != 1 and is_trap[next_node] == 1):
#                     if graph[next_node][now_node] != INF:
#                         print("nextnext ::: " + str(next_node))
#                         print("next_trap ::: " + str(is_trap))
#                         print("next state ::: " + str(state))
#                         heapq.heappush(priority, (now_node, weight + graph[next_node][now_node] , next_node, state))
#                 #둘다 함정이 작동 or 둘다 함정이 아님
#                 else:
#                     if graph[now_node][next_node] != INF:
#                         print("nextnext ::: " + str(next_node))
#                         print("next_trap ::: " + str(is_trap))
#                         print("next state ::: " + str(state))
#                         heapq.heappush(priority, (now_node, weight + graph[now_node][next_node], next_node, state))

#     return dijkstra()


# #print(solution(4, 1, 4, [[1, 2, 0], [2, 3, 2], [3, 2, 1], [4, 2, 5], [2, 4, 3]], [2]))
# #print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
# #print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 3], [2, 4, 2], [4, 2, 5], [2, 4, 5], [1, 4, 5]], [2, 3]))
# #print(solution(2, 1, 2, [[1, 2, 3], [2, 1, 1]], []) )