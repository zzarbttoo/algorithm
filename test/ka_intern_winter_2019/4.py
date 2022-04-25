from collections import defaultdict

import sys 
sys.setrecursionlimit(10 ** 4)

def solution(k, room_number):
    
    r = set()
    p = defaultdict(int)
    
    answer = []
    
    for room in room_number:
        now = room
        visit = [room]
        
        while now in r:
            now = p[now]
            visit.append(now)
            
        for v in visit:
            p[v] = now + 1
            
        r.add(now)
        answer.append(now)
        
    return answer