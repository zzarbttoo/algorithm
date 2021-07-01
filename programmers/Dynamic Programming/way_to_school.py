def solution(m, n, puddles):

    node_visited = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            #print("i ::: " + str(i) + " j ::: " + str(j))
            if i == 0 and j != 0:
                node_visited[i][j] = node_visited[i][j-1]
            elif j == 0 and i != 0:
                node_visited[i][j] = node_visited[i-1][j]
            elif i == 0 and j == 0:
                node_visited[i][j] = 1
            else:
                node_visited[i][j] = node_visited[i][j-1] + node_visited[i-1][j]
            if [j+1, i+1] in puddles:
                node_visited[i][j] = 0

    return node_visited[-1][-1] % 1000000007




m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))  