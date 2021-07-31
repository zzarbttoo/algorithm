def solution(N, A):
    init_num = [0 for i in range(N)]
    reset_num = [0 for i in range(N)]

    have_to_add_num = 0
    max_num = 0
    for i, num in enumerate(A):
        if num <= N:
            init_num[num-1] += 1
            max_num = max(max_num, init_num[num-1])

        elif max_num != 0:
            init_num.clear() 
            init_num += reset_num
            have_to_add_num += max_num
            max_num = 0
    return ([i + have_to_add_num for i in init_num])