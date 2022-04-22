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
            
            
            
            