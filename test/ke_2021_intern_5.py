from collections import defaultdict
import heapq

def solution(k, num, links):
    
    print(num)
    
    parent = defaultdict(lambda : -1)
    left = defaultdict(lambda : -1)
    right = defaultdict(lambda : -1)
    dp = defaultdict(int)
    
    leaf = []
    
    for i, link in enumerate(links):
        if link[0] != -1:
            left[i] = link[0]
            parent[link[0]] = i
        if link[1] != -1:
            right[i] = link[1]
            parent[link[1]] = i
        if link[0] == -1 and link[1] == -1:
            leaf.append(i)
            
    root = -1 
    
    for i in range(len(num)):
        if parent[i] == -1:
            root = i
    
    print(root)
    
    #parametric search 
    
    mini = 0 
    maxi = sum(num)
    
    while mini <= maxi:
        mid = (mini + maxi) // 2 
        break