from sys import stdin

def solution():
    #N = int(stdin.readline())
    #K = int(stdin.readline())

    N, K = 3, 7

    left, right = 1, N * N 
    answer = 0

    while left <= right:

        mid = left + (right - left) // 2 

        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)

        if count >= K:
            answer = mid 
            right = mid - 1
        else:
            left = mid + 1
    
    print(answer)


solution()
