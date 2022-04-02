from collections import defaultdict
from sys import stdin
from itertools import permutations


input = stdin.readline
    
def solution():
    N = int(input())
    c = list(map(int, input().split()))
    dis = defaultdict(list)
    answer = float('INF')

    for n in range(N):
        cnt = int(input())
        for _ in range(cnt):
            dis[n + 1].append(list(map(int, input().split())))

    order = list(permutations([i for i in range(1, N + 1)], N))

    for ord in order:
        money = 0
        temp = c[:]
        for o in ord:
            money += temp[o - 1]
            for d in dis[o]:
                temp[d[0] - 1] -= d[1]
                if temp[d[0] - 1] <= 0: temp[d[0] - 1] = 1
        if answer > money: answer = money
    
    print(answer)
                


    


solution()