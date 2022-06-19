# from collections import defaultdict
# import heapq

# def solution():
#     N = int(input())
#     di = defaultdict(list)
#     done = 0 

#     for i in range(N):
#         temp = list(map(int, input().split()))
#         done += 1 << i
#         for t in range(N):
#             if temp[t] != 0:
#                 di[i].append([t, temp[t]])
    

#     heap = []
#     for i in range(N):
#         heapq.heappush(heap, [0, i, i, 0])
    
#     answer = float('INF')
#     visit = defaultdict(lambda : defaultdict(lambda : float('INF')))
    
#     while heap:

#         wei, start, now, vi = heapq.heappop(heap)
#         vi += 1 << now 

#         if visit[now][vi] > wei:
#             visit[now][vi] = wei
#         else:
#             continue

#         for next in di[now]:
#             next_node, next_wei = next[0], next[1] + wei
#             if vi & (1 << next_node) == 0:
#                 heapq.heappush(heap, [next_wei, start, next_node, vi])
#             if vi == done and next_node == start:
#                 if answer > next_wei:
#                     print(next_wei)
    

# solution()

