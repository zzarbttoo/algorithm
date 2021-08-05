def solution(A):

    start_num, small_start_num, avg_num= 0 , 0 , 1000000
    length_A = len(A)
    
    if length_A == 2:
        return 0

    while True:
        now_avg = sum(A[start_num: start_num + 2])/2
        if avg_num > now_avg:
            avg_num , small_start_num = now_avg, start_num
        start_num += 1
        if start_num + 2 > length_A:
            break

    start_num = 0

    while True:
        #print(A[start_num: start_num + 3])
        now_avg = sum(A[start_num: start_num + 3])/3
        if avg_num > now_avg:
            avg_num , small_start_num = now_avg, start_num
        start_num += 1
        if start_num + 3 > length_A:
            break

    return small_start_num