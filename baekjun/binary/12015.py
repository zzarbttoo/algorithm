from sys import stdin
from bisect import bisect_left

def solution():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    #N, A = 8, [10, 20, 30 ,5, 10, 20, 30, 40]
    #N, A = 10, [4, 7, 10, 3, 1, 8, 7, 2, 5, 7]

    memo = [0]

    for a in A:
        print("a :::" + str(a))
        if memo[-1] < a:
            memo.append(a)
        else:
            memo[bisect_left(memo, a)] = a

    
    print(len(memo) - 1)


solution()

#bisect 이용