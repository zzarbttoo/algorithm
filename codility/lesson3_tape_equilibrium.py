import sys
def solution(A):
    sum_number = 0
    all_sum = sum(A)
    min_num = int(sys.maxsize)


    for i, num in enumerate(A):
        
        sum_number += num

        if i == len(A) - 1:
            return min_num
        
        print(i)
        min_num= min(abs(sum_number - (all_sum - sum_number)), min_num)
        print(sum_number)
        print(min_num)
    
    return min_num

print(solution([-1000, 1000]))