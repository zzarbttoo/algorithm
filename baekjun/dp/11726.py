def solution(n):
    count_array = [0 for _ in range(1000)]
    count_array[0] , count_array[1] = 1, 2

    for i in range(2, n):
        count_array[i] = count_array[i-1] + count_array[i-2]
        #print(count_array[i])
    return count_array[n-1] % 10007

    

print(solution(int(input())))