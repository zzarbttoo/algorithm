from sys import stdin 
from bisect import bisect_left

def solution():
    #N = int(stdin.readline())
    #L = list(map(int, stdin.readline().split()))
    N, L = 6, [4, 2, 6, 3, 1, 5]
    answer = [0]

    for l in L:
        if l > answer[-1]:
            answer.append(l)
        else:
            answer[bisect_left(answer, l)] = l
        
    print(len(answer) - 1)

solution()


