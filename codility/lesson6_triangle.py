def solution(A):
    length_A = len(A)
    sorted_A = sorted(A, reverse=True)

    now_num = 0
    #print(sorted_A)


    while now_num + 2 < length_A:
        #print(sorted_A[now_num], sorted_A[now_num+1], sorted_A[now_num+2])

        if sorted_A[now_num] + sorted_A[now_num + 1] > sorted_A[now_num+ + 2] and sorted_A[now_num + 1] + sorted_A[now_num + 2] > sorted_A[now_num] and sorted_A[now_num] + sorted_A[now_num + 2] > sorted_A[now_num+ + 1]:
            return 1

        now_num += 1

    return 0