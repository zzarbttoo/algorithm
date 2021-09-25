
def solution(A, B):
    # write your code in Python 3.6
    if len(B) == 0 :
        return 0
    
    count = 1
    last = B[0]
    for (start, end) in zip(A, B): 
        if start > last:
            count += 1 
            last = end 
        
    return count 
        