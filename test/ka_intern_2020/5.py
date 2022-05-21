from collections import defaultdict
from collections import deque

def solution(n, path, order):
    
    link = defaultdict(list)
    
    for l_path in path:
        link[l_path[0]].append(l_path[1])
        link[l_path[1]].append(l_path[0])
        
    
    parent = defaultdict(int)
    child = defaultdict(list)
    root = 0
    
    queue = deque([])
    
    for node in link[root]:
        queue.append([root, node])
    
    while queue:
        p, c = queue.popleft()
        parent[c] = p 
        child[p].append(c)
        
        for next in link[c]:
            if next != p:
                queue.append([c, next])
        
    