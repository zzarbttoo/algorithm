def solution(A, K):
    
    if len(A) == 0 or K == 0 or len(A) == 1:
        return A
    

    if K > len(A):
        K = K % len(A)   


    #print(A[-K:])
    #print(len(A)-K)
    #print(A[0:len(A)-K])

    return A[-K:] + A[0:len(A)-K]




    

    


    


    

# K = 3
# A = [3, 8, 9, 7, 6]

# print(solution(A, K))
# K = 4
# A = [1, 2, 3, 4]

# print(solution(A, K))
# K = 0
# A = []

# print(solution(A, K))

# K = 1
# A = [5, -1000]

K = 2
A = [1000]
print(solution(A, K))


                                                                                                                                                                                                                                                                                                                                                     