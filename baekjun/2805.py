from sys import stdin

def input_num():
    N, M = map(int, stdin.readline().split())
    H = list(map(int, stdin.readline().split()))

    return N, M, H

def soulution():
    N, M, H = input_num()
    H.sort()

    answer = -float('INF')
    left, right = 0, H[-1]

    while left <= right:
        mid = left + (right - left) // 2

        sum = 0  

        for h in H:
            if h > mid:
                sum += h - mid
        
        if sum >= M:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

 
soulution()