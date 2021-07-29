import sys
def solution(A):
    sum_number = 0
    all_sum = sum(A)
    min_num = int(sys.maxsize)


    for i, num in enumerate(A):
        
        sum_number += num

        if i == len(A) - 1:
            return min_num

        min_num= min(abs(sum_number - (all_sum - sum_number)), min_num)

    return min_num

print(solution([-1000, 1000]))