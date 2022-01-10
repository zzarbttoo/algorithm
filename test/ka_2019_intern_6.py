from collections import defaultdict
import sys 
sys.setrecursionlimit(10 ** 6)

def solution(n, path, order):
    
    #node_linked(양방향)
    n_l = defaultdict(list)
    v_o = defaultdict(lambda : -1)
    before_visited=[-1 for _ in range(n)]
    answer_visited = [1 for _ in range(n)]
    answer = False
    
    for p in path:
        n_l[p[0]].append(p[1])
        n_l[p[1]].append(p[0])
    
    for o in order:
        v_o[o[1]] = o[0]
        
    def dfs(now, before_visited):
        nonlocal n_l, answer_visited, answer, v_o
        #print(now, before_visited)
        
        now_visited = before_visited[:]
        now_visited[now] = 1 # visited
        
        #모두 visited이면 true return 
        if now_visited == answer_visited:
            answer = True
            return
        
        #다른 node 다 visited 이면서 연결되어 있는 부분의 우선 조건은 충족되지 않으면 return False
        be_vi = 0 #이전에 방문한 노드 갯수
        no_vi = 0 #방문하지 못하는 노드 갯수(조건 충족 X)
        for ne in n_l[now]:
            if now_visited[ne] == 1: be_vi += 1
            if v_o[ne] != -1 and now_visited[v_o[ne]] == -1:
                no_vi += 1
        
        if (be_vi + no_vi) == len(n_l[now]):
            return #answer = False
        
        #연결된 부분에 대해서 dfs 실행
        for ne in n_l[now]:
            #print(ne)
            #if now_visited[v_o[ne]] == -1: continue
            if v_o[ne] != -1 and now_visited[v_o[ne]] == -1: continue
            dfs(ne, now_visited[:])
        
        
    dfs(0, before_visited) #현재 node, before_v`isited, 
    #print(v_o)
    return answer