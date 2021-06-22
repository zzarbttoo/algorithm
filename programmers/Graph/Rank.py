import sys

def solution(n, results):

    INF = sys.maxsize

    dist = [[INF] * n for i in range(n)] #최댓값으로 초기화 

    #직접 연결된 부분 초기화(길이 1)
    for i, j in results:
        dist[i-1][j-1] = 1

    #자기 자신은 0으로 초기화 
    for i in range(n):
        dist[i][i] = 0
   
    for k in range(n): #가운데 노드 
        for i in range(n): #시작 노드 
            for j in range(n): #마지막 노드
                if dist[i][j] > dist[i][k] + dist[k][j]: #시작-끝 노드가 시작-중간+중간-끝 보다 작을 때 
                    dist[i][j] = dist[i][k] + dist[k][j] #변경한다

    
    for i in range(n):
        print()
        for j in range(n):

            if dist[i][j] == INF and  dist[j][i] != INF:
                dist[i][j] = - dist[j][i]
            
            if dist[i][j] != INF and dist[j][i] == INF:
                dist[j][i] = - dist[i][j]

    
    answer = 0
    for temp in dist: 
        if INF not in temp:
            answer += 1


    return answer

n = 5 
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))