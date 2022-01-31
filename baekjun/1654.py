from sys import stdin

def input_data():
    K, N = map(int, stdin.readline().split())
    H = []
    for _ in range(K):
        H.append(int(stdin.readline()))
    
    return K, N, H

def solution():
    K, N, H = input_data()
    H.sort()
    answer = - float('INF')

    left, right = 1, H[-1]

    while left <= right:
        mid = left + (right - left) // 2

        count = 0 

        for h in H:
            count += h // mid 

        if count >= N:
            answer = mid 
            left = mid + 1
        else:
            right = mid - 1
    
    print(answer)

solution()