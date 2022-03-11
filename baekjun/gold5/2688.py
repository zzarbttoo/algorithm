def input_():

    N = int(input())

    nums = []
    for _ in range(N):
        nums.append(int(input()))
    
    return nums

from collections import defaultdict
def solution():
    nums = input_()
    #nums = [2, 3, 4]

    memo = defaultdict(lambda : defaultdict(int))

    for i in range(10):
        memo[1][i] = 1
    
    for i in range(2, 65):
        for j in range(0, 10):
            for k in range(j, 10):
                memo[i][j] += memo[i - 1][k]

    for num in nums:
        sum = 0
        for i in range(0, 10):
            sum += memo[num][i]
        print(sum)
        
solution()