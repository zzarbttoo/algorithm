def solution(n, procession_array):
    memoization = [0 for _ in range(n)]

    if n == 1:
        return procession_array[0][0] * procession_array[0][1]


    # n이 1, 2일 경우에 대한 예외 처리 후 return
    memoization[1] = procession_array[0][0] * procession_array[0][1] * procession_array[1][1] # AB 

    for i in range(2, n):
        memoization[i] = min(memoization[i-1] + procession_array[i-2][0] * procession_array[i][0] * procession_array[i][1] 
        , memoization[i-2] + procession_array[i-1][0] * procession_array[i][0] * procession_array[i][1] + procession_array[i-2][0] * procession_array[i-2][1] * procession_array[i][1])

    return memoization[n-1]

n = int(input())
procession_array = []

for i in range(n):
    procession_array.append(list(map(int, input().split())))


print(solution(n, procession_array))

# n = 3
# procession_array = [[5,3], [3, 2], [2, 6]]
