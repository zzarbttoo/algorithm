from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    tw = deque(truck_weights)
    b = deque([0 for _ in range(bridge_length)])
    
    answer = 0
    time = 0
    sum_n = 0
    
    while tw:
        
        time += 1
        
        sum_n -= b.popleft()
        if sum_n + tw[0] <= weight:
            next_num = tw.popleft()
            sum_n += next_num
            b.append(next_num)
        else:
            b.append(0)
    
    
    while b:
        time += 1
        num = b.popleft()
        if num != 0:
            answer = time
    
    return answer