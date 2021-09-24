def solution(A):

    length = len(A)
    peak_array = []
    peak_true_array = [0 for _ in range(length)]

    for i, _ in enumerate(A):
        if i - 1 < 0:
            continue
                 
        if i + 1 >= length:
            continue
     
        if A[i-1] < A[i] and A[i+1] < A[i]:
            peak_array.append(i)
            peak_true_array[i] = 1
    
    peak_length = len(peak_array)

    if peak_length == 0: return 0 
    #print(peak_array)
 
    for block_size in range(peak_array[0] + 1, length + 1):
        block_num , possible = divmod(length, block_size)
        if possible != 0:
            continue

        #print(block_num, block_size)
        count = 0
        for idx in range(block_num):
            for i in range(idx * block_size, idx * block_size + block_size):
                if peak_true_array[i] == 1:
                    count += 1 
                    break 
        #print("count ::: " + str(count))
        if count == block_num:
            return block_num
            


print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
print(solution([1, 3, 2, 1])) # 
print(solution([5]))
print(solution([0, 1, 0, 0, 1, 0, 0, 1, 0]))