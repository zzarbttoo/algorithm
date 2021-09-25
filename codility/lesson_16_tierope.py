
def solution(K, A):

    count = 0 
    temp_sum = 0 

    for num in A:
        temp_sum += num 
        
        if temp_sum >= K:
            temp_sum = 0 
            count += 1 
    
    return count