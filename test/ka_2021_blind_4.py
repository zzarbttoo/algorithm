from collections import defaultdict

def solution(n, s, a, b, fares):
    
    fee = defaultdict(lambda : defaultdict(lambda : float("INF")))
    answer = float("INF")
    
    for fare in fares:
        fee[fare[0]][fare[1]] = fare[2]
        fee[fare[1]][fare[0]] = fare[2]
        
    for i in range(1, n + 1): fee[i][i] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                #조건문 추가 안할 시 시간 초과 발생
                if fee[i][j] > fee[i][k] + fee[k][j]: fee[i][j] = fee[i][k] + fee[k][j]
    
        
    for k in range(1, n + 1):
        answer = min(fee[a][k] + fee[b][k] + fee[k][s], answer)
    
    return answer
        
        
        
    
    
    