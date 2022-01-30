def solution(distance, rocks, n):
    mi = 0 #거리의 최솟값 
    ma = distance #거리의 최댓값
    answer = - float('INF')
    
    left, right = mi, ma
    rocks.sort()
    
    while left <= right:
        mid = left + (right - left) // 2 #거리의 중간값
        cur = 0 #현재 위치
        remove = 0
        min_num = float('INF')
        
        for rock in rocks:
            diff = rock - cur 
            
            if diff < mid:
                remove += 1 
            else:
                cur = rock
                min_num = min(min_num, diff)
                
        if remove > n: right = mid - 1
        else:
            answer = max(min_num, answer)
            left = mid + 1
            
    return answer
                
            