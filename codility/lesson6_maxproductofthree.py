import math
def solution(A):

    length_A = len(A)
    if length_A== 3:
        return A[0] * A[1] * A[2]
 
    sorted_A = sorted(A)
    #print(sorted_A)

    min_num_multiply = sorted_A[0] * sorted_A[1]
    max_num_multiply = sorted_A[length_A - 3] * sorted_A[length_A - 2]
    last_num = sorted_A[length_A-1]

    #print(min_num_multiply, max_num_multiply, last_num)
    answer = last_num * max(min_num_multiply, max_num_multiply) if last_num >= 0 else last_num * min(min_num_multiply, max_num_multiply)



    return answer# Import math Library