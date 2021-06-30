def solution(n, costs):

    costs.sort(key = lambda cost:cost[2], reverse = True) #가중치 내림차순 정렬(pop()으로 하려고)

    node_root = dict()

    #root node 자기 자신으로 초기화  #parent node 초기화 
    for i in range(n):
        node_root[i] = i

    
    def find(u):
        if u != node_root[u]:
            node_root[u] = find(node_root[u])
        return node_root[u]


    #u, v를 연결할 것이기 때문에, v의 root 를 u의 root로 바꾼다 
    def union(u, v):
        u_parent = find(u)
        v_parent = find(v)
        node_root[v_parent] = u_parent 


    minimum_cost = 0

    while costs:
        u, v, weight = costs.pop() 
        if find(u) != find(v):
            union(u, v)
            minimum_cost += weight


    return minimum_cost




n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))