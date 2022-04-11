from collections import defaultdict
from xml.etree.ElementInclude import include

def solution():
    N = int(input())
    B = list(map(int, input().split()))

    incline = defaultdict(lambda : defaultdict(float))
    answer = 0


    for y in range(N):
        for x in range(N):
            if x == y: incline[y][x] = 0
            else: incline[y][x] = (B[y] -B[x]) / (y - x)

    for k, v in incline.items():
        print(k, v)
    
    for b in range(N):
        print("b ::: " +str(b))
        sum = 0
        b_n = float('INF')
        for f in range(b - 1, -1, -1):
            if b_n <= incline[b][f]: continue
            b_n = incline[b][f]
            print(b_n)
            sum += 1

        b_n = -float('INF')
        for n in range(b + 1, N):
            if b_n >= incline[b][n]: continue
            b_n = incline[b][n]
            sum += 1
        print("sum ::: " + str(sum))
        if answer < sum: answer = sum

    print(answer)
    
solution()