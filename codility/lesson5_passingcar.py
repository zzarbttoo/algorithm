def solution(A):
    sum_before_west , answer = 0, 0
    all_sum = sum(A)

    for i in A:
        if i == 1:
            sum_before_west += 1
        else:
            answer += (all_sum - sum_before_west)
    
    return answer if answer <= 1000000000 else -1

