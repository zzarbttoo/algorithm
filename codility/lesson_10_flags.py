def solution(A):

    length = len(A)
    peak_array = [0 for _ in range(length)]
    peak_length = 0
    for i, _ in enumerate(A):
        if i - 1 < 0:
            continue
        
        if i + 1 >= length:
            continue
     
        if A[i-1] < A[i] and A[i+1] < A[i]:
            peak_array[i] = 1
            peak_length += 1 
            print(i)

    next_peak = [0 for _ in range(length)]

    next_peak[-1] = -1
    for i in range(length - 2, -1, -1):
        if peak_array[i] == 1:
            next_peak[i] = i
        else:
            next_peak[i] = next_peak[i+1]

    
    flag = 1 
    result = 0 

    #print(next_peak)

    while flag <= length:
        pos = 0 
        num = 0 
        while pos < length and num < flag:
            pos = next_peak[pos]
            #print("pos :: " + str(pos))
            if pos == -1:
                break 
            num += 1 
            pos += flag 
        result = max(result, num)
        flag += 1 
    return result 
    
    



    
    
    





print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))