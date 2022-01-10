from collections import defaultdict

def solution(n, path, order):
    
    #node_linked(양방향)
    n_l = defaultdict(list)
    v_o = defaultdict(lambda : defaultdict(int))
    before_visited=[-1 for _ in range(n)]
    answer_visited = [1 for _ in range(n)]
    answer = False
    
    for p in path:
        n_l[p[0]].append(p[1])
        n_l[p[1]].append(p[0])
    
    for o in order:
        v_o[o[0]][o[1]] = -1 #먼저 방문 해야함
        v_o[o[1]][o[0]] = 1 #나중에 방문해야함
        
    def dfs(now, before_visited, vis):
        nonlocal n_l, answer_visited, answer
        
        #True가 하나라도 나왔으면 진행 안함
        if answer == True:
            return 
        
        now_visited = before_visited[:]
        now_visited[now] = 1 # visited
        
        #모두 visited이면 true return 
        if before_visited == answer_visited:
            answer = True
            return
        
        #다른 node 다 visited 이면서 연결되어 있는 부분의 우선 조건은 충족되지 않으면 return False
        be_vi = 0 #이전에 방문한 노드 갯수
        no_vi = 0 #방문하지 못하는 노드 갯수(조건 충족 x)
        for ne in n_l[now]:
            if now_visited[ne] == 1: be_vi += 1
            if 
            
        
        #연결된 부분에 대해서 dfs 실행
        #for ne in n_l[now]:
            #n_v_o = v_o.copy()
            #현재 방문에 대한 n_v_o 처리
            # no_vi 에 대해 방문 처리
            
            #dfs(ne, now_visited.copy(), n_v_o)