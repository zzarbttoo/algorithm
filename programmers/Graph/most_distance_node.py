import collections
import heapq
def solution(n, edge):


   graph = collections.defaultdict(list)

   for start, end in edge:
      graph[start].append(end)
      graph[end].append(start)
   
   print(graph)

   Q = [(0, 1)]

   dist = collections.defaultdict(int)

   while Q:
      time, node = heapq.heappop(Q)
      if node not in dist:
         dist[node] = time
         for v in graph[node]:
            alt = time + 1
            heapq.heappush(Q, (alt, v))
   
   distance_value = list(dist.values())
   return distance_value.count(max(distance_value))
   



      
      





      






   return


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))